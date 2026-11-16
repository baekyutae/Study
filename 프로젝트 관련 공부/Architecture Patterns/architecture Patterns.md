
## 1. Monolith vs Microservices (MSA)

### 개념 비교
* **Monolith (모놀리스):** 하나의 소프트웨어를 구성하는 모든 모듈과 코드를 한 프로젝트에서 관리하는 것을 말한다.<br>
  시스템 설계 시 데이터 일관성 확보와 내부 통신의 효율성을 최우선으로 고려할 때 주로 채택
  
* **Microservices (MSA):** 하나의 소프트웨어를 구성하는 컴포넌트들을 독립적인 프로젝트들로 분리하여 관리하는 것을 말한다.<br>
  각각의 컴포넌트들을 마이크로 서비스라고 부를 수 있다.
  개발과 배포도 이렇게 분리된 마이크로서비스 단위로 진행

### 장단점 비교

**Monolith (모놀리스) 

장점
단점

모노리스 분해 패턴: https://docs.aws.amazon.com/ko_kr/prescriptive-guidance/latest/modernization-decomposing-monoliths/decomposing-patterns.html


> **💡 핵심 전략: Monolith-First**
> 처음부터 MSA로 시작하면 오버엔지니어링(인프라 비용/시간 낭비)의 위험이 크다. 도메인 경계가 명확해지고 특정 기능에 병목이 생길 때 점진적으로 분리하는 것이 이상적이다.

---

## 2. 서비스 간 통신: Sync vs Async

MSA 환경에서 분리된 서비스 간의 데이터 교환 방식.

* **Sync (동기 통신)**
  * **방식:** HTTP REST API 등. 요청 후 응답이 올 때까지 대기.
  * **특징:** 직관적이고 즉각적이나, 상대 서버가 느려지면 내 서버도 병목에 걸림(강한 결합).
* **Async (비동기 통신)**
  * **방식:** Message Queue (Kafka, RabbitMQ) 활용.
  * **특징:** 이벤트를 큐에 던져두고 내 할 일을 함. 장애가 전파되지 않고 트래픽 버퍼링이 가능하지만, **데이터 정합성(예: DB 저장 실패 시 큐 전송 취소 등)** 관리가 매우 중요함.

---

## 3. Serverless (FaaS - Function as a Service)

서버 관리를 클라우드에 위임하고, 오직 '코드(함수)' 단위로 배포하고 실행하는 아키텍처. (예: AWS Lambda)

* **비용 모델:** 서버를 띄워두는 시간(월세)이 아닌, 함수가 **실행된 횟수와 시간**만큼만 비용 지불.
* **Cold Start (콜드 스타트):** * 오랫동안 호출이 없다가 실행될 때, 컨테이너를 새로 띄우고 초기화하느라 첫 응답이 매우 느려지는 현상.
  * **AI/ML 추론 서비스 적용 시 주의:** 무거운 모델 가중치를 메모리에 로드하는 시간 + 콜드 스타트가 겹치면 실시간 서비스(사용자 대면)에는 치명적일 수 있음.
* **적합한 Use Case:**
  * 간헐적인 백그라운드 배치 작업 (하루 한 번 정산 등).
  * 트래픽 예측이 불가능한 이벤트 기반 작업.
  * S3 이미지 업로드 시 썸네일 생성, 혹은 비동기 AI 파이프라인 (영상 자막 추출 등).

---

## 4. The Twelve-Factor App

클라우드 네이티브(MSA) 환경에서 튼튼하고 유연한 백엔드 앱을 만들기 위한 12가지 원칙.

### 실무 기준 Tier 1 (절대 타협 불가)
1. **Config (설정):** 환경 변수 분리. DB 비밀번호나 API 키를 절대 코드에 하드코딩하지 말 것. (보안 및 환경 분리 목적)
2. **Codebase (코드베이스):** 하나의 Git 저장소로 형상 관리.
3. **Dependencies (종속성):** 명시적 선언 (`requirements.txt`, `Pipfile` 등).
4. **Processes (프로세스):** 앱은 무상태(Stateless)로 실행. 세션 상태는 캐시/DB에 위임.

### Tier 2 (클라우드/컨테이너 핵심)
5. **Dev/Prod Parity:** 개발/운영 환경의 최대한 일치 (Docker 활용).
6. **Disposability:** 빠른 시작과 안전한 종료 (Graceful shutdown).
7. **Logs:** 로그는 파일이 아닌 이벤트 스트림(표준 출력)으로 취급.
8. **Backing Services:** DB, 큐 등은 언제든 교체 가능한 첨부 자원으로 취급.

### 💻 Python Config 환경 변수 적용 예시

```python
# ❌ 하드코딩 (보안 위험, 깃허브 유출 주의)
# DATABASE_URL = "mysql://admin:password123@live-db.com/mydb"

# ✅ 12-Factor 원칙 준수 (운영체제 환경 변수에서 읽어오기)
import os

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL이 설정되지 않았습니다.")

```

### 1. Monolith vs Microservices (MSA) 딥다이브

Monolith에서 MSA로 넘어갈 때 가장 큰 허들은 '코드의 분리'가 아니라 '데이터의 분리'입니다.

- **Strangler Fig Pattern (스트랭글러 피그 패턴):** 기존 Monolith를 한 번에 엎는 것이 아니라, 새로운 기능을 점진적으로 MSA로 빼내면서 기존 시스템을 서서히 대체하는 실무적인 마이그레이션 전략입니다.
    
    - **Database per Service & 분산 트랜잭션:** MSA에서는 각 서비스가 독립적인 DB를 가지는 것이 이상적입니다. 이때 결제 서비스와 재고 서비스 간의 트랜잭션을 어떻게 보장할 것인가? (예: **SAGA 패턴**, 2PC)
        
- **CQRS (Command and Query Responsibility Segregation):** 상태를 변경하는 명령(Command)과 조회(Query) 모델을 분리하여, 복잡한 조인이 필요한 MSA 환경에서 읽기 성능을 최적화하는 기법입니다.
    

### 2. Sync vs Async (서비스 간 통신) 딥다이브

이벤트를 큐에 던져두는 비동기 방식은 유연하지만, 실패에 대한 대비가 필수적입니다.

- **멱등성 (Idempotency):** 네트워크 장애로 인해 클라이언트가 재시도(Retry)를 했을 때, API가 여러 번 호출되어도 서버의 상태(결과)는 동일하게 유지되어야 합니다. (예: 결제 요청 시 고유한 `Idempotency-Key` 사용)
    
- **DLQ (Dead Letter Queue):** 카프카(Kafka)나 래빗MQ(RabbitMQ)에서 메시지 처리(Consumer)가 계속 실패할 경우, 무한 루프에 빠지지 않도록 실패한 메시지만 따로 모아두는 큐입니다.
    
    - **Eventual Consistency (최종 일관성):** 동기식처럼 즉각적인 데이터 일치는 포기하되, '결과적으로는' 모든 시스템의 데이터가 일치하게 된다는 비동기 통신의 핵심 개념입니다.
        

### 3. Serverless (FaaS) 딥다이브

비용 효율적이고 이벤트 기반 작업에 적합하지만, 관계형 데이터베이스(RDBMS)와 만났을 때 예상치 못한 병목이 생깁니다.

- **DB Connection Pooling 문제:** 람다(Lambda)와 같은 FaaS는 호출될 때마다 컨테이너가 뜨기 때문에, 트래픽이 몰리면 DB 커넥션을 순식간에 고갈시킵니다. 이를 해결하기 위한 **RDS Proxy**나 Connection Pooler 아키텍처를 이해하는 것이 중요합니다.
    
    - **Cold Start 완화 전략:** 무거운 가중치를 로드해야 하는 AI 모델을 FaaS로 서빙해야만 한다면, 미리 컨테이너를 데워두는 **Provisioned Concurrency (프로비저닝된 동시성)** 등의 클라우드 기능을 활용해 지연 시간을 줄이는 방법을 고민해볼 수 있습니다.
        

### 4. The Twelve-Factor App 딥다이브

단순한 개념을 넘어 실제 파이썬(Python) 애플리케이션 코드로 어떻게 구현할지가 관건입니다.

- **Config (설정)의 진화:** 환경 변수 분리를 넘어, 실무에서는 DB 비밀번호나 API 키 같은 민감 정보를 AWS Secrets Manager나 HashiCorp Vault 같은 중앙 집중식 비밀물 관리(Secrets Management) 서비스로 관리하여 보안을 강화합니다.
    
- **Disposability (폐기 가능성)와 Graceful Shutdown:** 앱이 종료될 때 진행 중이던 요청이나 DB 트랜잭션이 끊기지 않도록, 파이썬에서 `SIGTERM` 시그널을 가로채어 안전하게 리소스를 정리하고 종료하는 코드를 작성하는 방법입니다.
    
- **Backing Services:** 언제든 교체 가능한 자원으로 취급하기 위해, 코드 내에서 특정 DB 벤더(예: MySQL 특화 쿼리)에 강하게 결합하기보다는 ORM(예: SQLAlchemy)의 추상화 계층을 적절히 활용하는 전략입니다.