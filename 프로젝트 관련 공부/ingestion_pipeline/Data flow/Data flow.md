
### Step 1. 업로드 요청 & 직접 업로드 (Client $\rightarrow$ Storage)

서버를 거치지 않고 스토리지로 직행하는 **Presigned URL** 패턴.

#### 1. 데이터 종류 (Payload)

- **요청 (Client $\rightarrow$ API Gateway):**
    
    - **Format:** JSON
        
    - **Content:** `{ "file_name": "lecture_01.mp4", "file_size": 104857600, "mime_type": "video/mp4" }`
        
    - **확장자:** `.mp4`, `.mov`, `.avi`, `.mkv` (영상 컨테이너 포맷)
        
- **업로드 (Client $\rightarrow$ Object Storage):**
    
    - **Format:** Binary Stream (Raw Bytes)
        
    - **Header:** `Content-Type: video/mp4`
        

#### 2. 전송 툴 및 원리

- **HTTP/1.1 or HTTP/2 (PUT Request):**
    
    - API 서버가 AWS S3(혹은 GCS) SDK를 사용해 "5분 동안만 유효한 임시 업로드 권한(Presigned URL)"을 생성해 클라이언트에 준다.
        
    - 클라이언트는 이 URL로 바이너리 데이터를 직접 `PUT`
        
[[추상화 전략과 의존성 역전]]


#### 3. 선택지와 트레이드 오프

|**방식**|**설명**|**장점**|**단점**|**선정 이유**|
|---|---|---|---|---|
|**Presigned URL (채택)**|클라이언트가 스토리지에 직접 업로드|**서버 부하 Zero**, 구현 비용 저렴|보안 설정(CORS 등)이 까다로움|**비디오는 대용량 트래픽이므로 백엔드 서버를 통과시키면 안 됨**|
|**Server Proxy**|클라이언트 $\rightarrow$ 서버 $\rightarrow$ 스토리지|구현이 쉽고 중앙 제어 용이|서버의 Network I/O 고갈, 비용 폭증|대용량 파일 처리 부적합|
|**Multipart Upload**|파일을 5MB 단위로 쪼개서 병렬 업로드|속도 빠름, 실패 시 이어 올리기 가능|클라이언트 로직이 복잡해짐|파일 크기가 GB 단위라면 필수 고려 (현재 기획서엔 명시 없으나 권장)|

---

### Step 2. 파이프라인 트리거 (API server ->  Broker)

파일이 안착했음을 알리는  단계.

#### 1. 데이터 종류

- **Job Task Message (JSON):**
    
    - 단순 파일 정보뿐만 아니라 사용자 식별자, DB PK, 처리 옵션 등 비즈니스 문맥(Context)을 포함한 메시지 객체다.
        
    - **형식:**

```JSON
{
  "task_type": "ingestion",
  "payload": {
    "video_id": "550e8400-e29b...",     // DB Primary Key (필수)
    "user_id": "user_123",             // 사용자 격리 및 과금용
    "bucket": "biblio-video-store",
    "key": "videos/raw/uuid-1234.mp4", // 파일 경로
    "options": {                       // 사용자 요청 옵션(미정)
       "language": "ko",
       "model": "high_quality"
    }
  }
}

```

#### 2. 전송 툴 및 원리

- **Message Broker Client Library (Producer):**
    
    - API 서버(FastAPI) 내부 로직에서 `pika`나 `celery` 같은 클라이언트 라이브러리를 통해 브로커(RabbitMQ/Redis)에 직접 연결한다.
        
    - DB 트랜잭션(메타데이터 저장)이 성공하면, `publish()` 메서드를 호출하여 **Task Queue**에 메시지를 적재한다.
        
- 발행 흐름

	1. 완료 요청 (Client → Server):
    
	    - 클라이언트가 스토리지 업로드 성공(200 OK) 직후, 서버에 `POST /upload-complete`를 호출한다.
        
	2. **DB 갱신 (Server → DB):**
    
	    - 서버는 해당 비디오의 상태를 `UPLOADING`에서 `PENDING`으로 갱신한다.
        
	3. **메시지 전송 (Server → Broker):**
    
    - 트랜잭션 내에서 브로커의 Queue로 작업 메시지를 발행한다.

	4. **응답 반환 (Server → Client):**
    
    - **중요:** 서버는 처리가 끝날 때까지 기다리지 않고 **즉시 응답**한다.
        
    - **Status Code:** `202 Accepted` (요청은 접수되었으나 처리는 완료되지 않음).
        
    - **Response Body:**

``` json
 {
          "message": "Processing started",
          "video_id": "550e8400-e29b...",
          "status": "PENDING",
          "check_status_url": "/api/videos/550e8400.../status" // 폴링용 URL 제공
        }

```


- **클라이언트 동작 (Client Side):**
    
    - 응답을 받으면 UI를 "처리 중(Processing...)"으로 변경하고, 제공받은 URL로 주기적으로 상태를 조회(Polling)하거나 웹소켓 대기를 시작한다.


#### 3. 선택지와 트레이드 오프

[[업로드 트리거 트레이드 오프]]


---

### Step 3. 오디오 추출 (Media Worker)

CPU를 태워서 포맷을 변경하는 **ETL(Extract, Transform, Load)** 단계

#### 1. 데이터 종류

- **Input:** Video Binary (`.mp4`) - 스토리지에서 스트리밍으로 읽음.
    
- **Output:** Audio Binary (`.mp3` or `.wav`)
    
	추출한 오디오는 다시 storage에 저장(원본 영상과 매핑)

| **구분**     | **경로 구조 (Path)**                        | **비고**           |
| ---------- | --------------------------------------- | ---------------- |
| **원본 영상**  | `videos/{video_id}/original.mp4`        | 사용자 업로드 파일       |
| **추출 오디오** | `videos/{video_id}/audio_extracted.mp3` | Media Worker가 생성 |

#### 2. 전송 툴 및 원리

- **FFmpeg (Subprocess):**
    
    - 워커 내부에서 FFmpeg 프로세스를 실행하여 비디오 트랙을 제거하고 오디오 트랙만 인코딩
        
    - 명령어 예시: `ffmpeg -i input.mp4 -vn -acodec libmp3lame -q:a 2 output.mp3`
        

#### 3. 선택지와 트레이드 오프

**영상 포맷**

|**포맷/도구**|**장점**|**단점**|**선정 이유 & Senior's Tip**|
|---|---|---|---|
|**MP3 (채택)**|**용량이 작음 (WAV 대비 1/10)**|손실 압축으로 음질 저하 (미세)|**외부 STT API 전송 시 네트워크 비용과 속도(Latency)가 중요하므로 용량이 작은 MP3가 유리함**|
|**WAV (PCM)**|무손실, STT 인식률 미세하게 높음|용량이 너무 큼|로컬 모델(Whisper)을 돌린다면 WAV가 좋지만, API 전송 시 비효율적|
|**AAC (.m4a)**|MP3보다 압축 효율 좋음|일부 레거시 시스템 호환성 이슈|MP3가 가장 무난함|

**영상 -> 텍스트 툴**

 (1) 로컬 프로세싱 (Self-Hosted) 방식

| **기술 스택**        | **특징**                  | **장점**                                   | **단점**                             |
| ---------------- | ----------------------- | ---------------------------------------- | ---------------------------------- |
| **FFmpeg (CLI)** | 로우레벨 바이너리 직접 호출         | 가장 빠르고 모든 포맷 지원, 레퍼런스 방대                 | 프로세스 제어(Zombie Process 등) 관리가 까다로움 |
| **PyAV**         | FFmpeg의 C-Binding 라이브러리 | Python 내부에서 바이너리 데이터로 직접 접근 가능하여 오버헤드 적음 | 사용법이 매우 복잡하고 학습 곡선이 높음             |
| **MoviePy**      | Python 기반 고수준 편집 라이브러리  | 코드가 간결하고 읽기 쉬움 (Pythonic)                | 내부적으로 FFmpeg을 다시 호출하므로 속도가 느리고 무거움 |
| **GStreamer**    | 파이프라인 기반 미디어 프레임워크      | 스트리밍 처리에 최적화, 하드웨어 가속 연동 용이              | 설정 및 파이프라인 설계가 FFmpeg보다 훨씬 복잡함     |

(2) 클라우드 매니지드 (Managed Service) 방식

|**기술 스택**|**특징**|**장점**|**단점**|
|---|---|---|---|
|**AWS Elemental MediaConvert**|AWS 전용 트랜스코딩 서비스|서버 관리 제로, 대규모 병렬 처리 보장, 고신뢰성|비용이 비쌈, AWS 에코시스템에 종속(Lock-in)됨|
|**GCP Transcoder API**|Google Cloud 전용 서비스|Vertex AI 등 타 구글 서비스와 연동성 우수|영상 길이/개수에 따른 비용 발생, 커스텀 설정 제약|
|**Serverless (AWS Lambda + FFmpeg Layer)**|람다 함수에 FFmpeg 실행 파일 포함|사용한 만큼만 비용 지불, 자동 스케일링|람다 실행 시간/메모리 제한으로 대용량(GB 단위) 처리 불가|



---

### Step 4. AI 분석 (AI Worker $\rightarrow$ External API : STT Model)

외부 시스템과 통신하므로 **네트워크 I/O**와 **데이터 직렬화**가 핵심인 단계.

#### 1. 데이터 종류

- **Input (Request):** Audio Binary (Base64 encoded) or GCS URI (클라우드 경로).
    
- **Output (Response):** JSON (Transcript + Timestamp)
    
    - **형식:**

 ```JSON
        {
          "results": [
            { "transcript": "안녕하세요", "start_time": 0.0, "end_time": 1.5 },
            { "transcript": "오늘의 주제는...", "start_time": 1.5, "end_time": 3.2 }
          ]
        }
 ```


- **Embedding Output:** Float32 Array (Vector)
    
    - 예: `[0.123, -0.521, 0.003, ...]` (보통 768차원 또는 1536차원)
        

#### 2. 전송 툴 및 원리

- **gRPC or REST over HTTP/2:**
    
    - Google Vertex AI는 gRPC를 권장하며, 대용량 오디오 전송 시 스트리밍을 지원.
        
    - 파이썬 클라이언트(`google-cloud-speech`)가 내부적으로 통신을 처리합니다.
        

#### 3. 선택지와 트레이드 오프

|**방식**|**설명**|**장점**|**단점**|**선정 이유**|
|---|---|---|---|---|
|**Cloud STT (Vertex AI) (채택)**|구글 서버에 오디오 전송 후 텍스트 수신|**높은 정확도**, 관리 포인트 없음, 다국어 지원|비용 발생, 네트워크 지연(Latency)|**운영 복잡도를 낮추고 STT 품질을 보장하기 위해 채택**|
|**Local STT (Whisper)**|GPU 워커에서 직접 모델 구동|데이터 보안 우수, 추가 비용 없음(서버비 제외)|GPU 인스턴스 관리 복잡, 스케일링 어려움|초기 스타트업 단계에선 관리 비용이 더 큼|
|**Sync vs Async API**|동기 요청 vs 비동기 작업 요청|긴 영상(1분 이상)은 비동기(LongRunningRecognize) 필수|코드 복잡도 증가|영상 길이에 따라 자동 분기 처리 필요|

---

### Step 5. 데이터 저장 (Index Worker $\rightarrow$ DBs)

데이터의 **정합성(Consistency)**과 **검색 성능**을 결정짓는 최종 단계입니다.

#### 1. 데이터 종류

- **RDB (PostgreSQL):** 정형 데이터
    
    - Schema: `video_id (UUID)`, `script (Text)`, `meta_info (JSONB)`
        
- **Vector DB (Pinecone/Weaviate):** 고차원 벡터 데이터
    
    - Schema: `id (UUID)`, `values (List[float])`, `metadata ({start: 0.5, end: 1.0, text: "..."})`
        

#### 2. 전송 툴 및 원리

- **Connection Pool (SQLAlchemy / Psycopg2):**
    
    - TCP 연결을 맺고 SQL(`INSERT`)을 실행합니다.
        
- **HTTP/REST or gRPC (Vector DB Client):**
    
    - 벡터 데이터는 보통 HTTP 기반의 API로 전송합니다 (Pinecone 등 SaaS 이용 시).
        

#### 3. 선택지와 트레이드 오프

|**기술**|**설명**|**장점**|**단점**|**선정 이유**|
|---|---|---|---|---|
|**Vector DB + RDB (채택)**|메타데이터는 RDB, 검색용 벡터는 전용 DB|**각 목적에 최적화된 성능** (RDB: 트랜잭션, Vector DB: 유사도 검색)|두 DB 간 데이터 동기화(Consistency) 문제 발생 가능|**검색 품질과 데이터 무결성 두 마리 토끼를 잡기 위함. 정합성은 트랜잭션/Saga 패턴으로 보완**|
|**Pgvector (Postgres Only)**|PostgreSQL에 벡터 플러그인 설치|단일 DB로 관리 용이, 트랜잭션 보장|전용 벡터 DB보다 대규모 검색 성능 낮을 수 있음|초기 단계라면 Pgvector도 강력 추천하나, 확장성을 위해 분리 설계된 것으로 보임|
|**Sync Insert**|건건이 Insert|구현 단순|대량 데이터 저장 시 느림|**Batch Insert (Bulk)**를 사용하여 수천 개의 벡터를 한 번에 밀어넣어야 함|

---

### 💡 Senior Developer's Final Review

이 파이프라인에서 당신이 가장 신경 써야 할 **숨겨진 병목(Hidden Bottleneck)**은 다음과 같습니다.

1. **Network Bandwidth:** Media Worker가 영상을 다운로드하고 다시 업로드할 때 대역폭을 엄청나게 씁니다. 같은 리전(Region) 내의 스토리지와 컴퓨팅 자원을 사용하여 전송 비용을 '0'으로 만들고 속도를 높이세요.
    
2. **API Rate Limit:** Vertex AI나 Vector DB는 분당 요청 제한(Quota)이 있습니다. AI Worker가 무턱대고 요청을 쏘면 `429 Too Many Requests` 에러가 납니다. **Token Bucket** 알고리즘 같은 Rate Limiter가 반드시 필요합니다.
    
3. **Data Consistency:** RDB엔 저장됐는데 Vector DB 저장 중 에러가 나면? 검색은 안 되는데 상세 페이지는 뜨는 유령 데이터가 생깁니다. Index Worker에서 **트랜잭션 롤백** 처리를 아주 꼼꼼하게 짜야 합니다.
    

이 설명이 구현에 명확한 가이드가 되었기를 바랍니다. 혹시 `Rate Limiter` 구현체나 `Vector DB` 스키마 설계가 궁금하시다면 말씀해 주세요.