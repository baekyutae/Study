---
tags:
  - 네트워크
  - 가용성
  - 로드밸런싱
  - 프록시
created: 2026-05-28
source: 혼자공부하는네트워크
chapter: "7-1"
---

# Chapter 7-1. 안정성을 위한 기술

> [!abstract] 한 줄 요약
> 100% 장애 없는 시스템은 불가능하다. **장애가 발생해도 서비스가 계속되도록** 설계하는 기술들 — 이중화, 로드 밸런싱, 프록시.

---

## 🛡️ 가용성

### 안정성 · 가용성 · 고가용성

- **안정성 (Reliability)** — 시스템이 오류 없이 지속적으로 정상 동작하는 정도. "얼마나 자주 고장 나지 않는가"에 초점.
- **가용성 (Availability)** — 전체 사용 시간 중 시스템이 정상 서비스 가능한 시간의 비율.
  $$\text{가용성} = \frac{\text{업타임}}{\text{업타임} + \text{다운타임}}$$
- **고가용성 (HA, High Availability)** — 가용성을 매우 높게 유지하도록 설계된 시스템.

> [!info] 가용성 수치 감각
> | 수준 | 가용성 | 연간 다운타임 |
> | --- | --- | --- |
> | Three Nines | 99.9% | 약 8시간 45분 |
> | Four Nines | 99.99% | 약 52분 |
> | **Five Nines** | **99.999%** | **약 5분** |

### 업타임 · 다운타임

- **업타임 (Uptime)** — 시스템이 정상 작동한 시간.
- **다운타임 (Downtime)** — 시스템이 중단된 시간.
	- 계획된 점검 (planned)
	- 비계획된 장애 (unplanned)

### 결함 감내 (Fault Tolerance)

일부 구성 요소에 결함이 생기더라도 전체 시스템은 계속 동작하도록 설계하는 기법.

> [!important] 핵심 사상
> **100% 원천 차단은 불가능**하다.
> 문제가 _"발생하지 않게"_ 가 아니라 _"발생해도 서비스가 계속되도록"_ 설계한다.

---

## 🔁 이중화 (Redundancy)

### SPOF (Single Point Of Failure, 단일 장애점)

- 그 부분 하나가 고장 나면 전체 시스템이 멈추는 지점.
- **이중화의 목적 = SPOF 제거.**

### 액티브/스탠바이 vs 액티브/액티브

| 구분 | 액티브/스탠바이 | 액티브/액티브 |
| --- | --- | --- |
| 동작 | 한쪽만 서비스, 나머지 대기 | 모두 동시에 서비스 |
| 장애 시 | 페일오버로 전환 | 그대로 분산 유지 |
| 자원 활용 | 절반은 노는 상태 | 모두 활용 |
| 복잡도 | 단순 | 상태 동기화·세션 일관성 필요 |

### 다중화

이중화(2개)를 넘어 3중, N중으로 구성. **가용성↑, 비용↑.**

### 티밍 (Teaming) · 본딩 (Bonding)

- 여러 NIC(네트워크 카드)을 묶어 하나의 논리 인터페이스로 사용.

| 용어 | 사용 OS |
| --- | --- |
| **티밍** | Windows |
| **본딩** | Linux |

목적:
- 대역폭 증가 (로드 밸런싱)
- 장애 대비 (Fault Tolerance)

---

## ⚖️ 로드 밸런싱

### 트래픽

네트워크상에 흐르는 데이터의 양. 특정 시점 트래픽이 서버 처리 한계를 넘으면 응답 지연·장애 발생.

### 로드 밸런싱 · 로드 밸런서

- **로드 밸런싱 (Load Balancing)** — 트래픽을 여러 서버에 골고루 분산.
- **로드 밸런서 (Load Balancer)** — 분산을 수행하는 장비/소프트웨어.
	- 클라이언트는 LB 한 곳만 바라봄
	- LB가 뒤단(backend) 서버를 골라 요청 전달

### L4 / L7 로드 밸런싱

| 구분 | L4 | L7 |
| --- | --- | --- |
| 계층 | 전송 계층 (IP + 포트) | 응용 계층 (HTTP URL/헤더/쿠키) |
| 속도 | 빠름, 부하 적음 | 처리 비용↑ |
| 라우팅 | 단순 분산 | URL별·사용자별 똑똑한 라우팅 |
| 패킷 내용 | 안 봄 | 봄 |

#### L4 vs L7 — 언제 무엇을 쓰나?

> [!warning] 흔한 오해
> "MSA 아니면 L4면 된다" → **❌**
> HTTP/HTTPS 웹 서비스는 **모놀리식이어도 거의 L7이 기본**.

##### 모놀리식인데도 L7이 필요한 이유

1. **HTTPS의 SSL 종료 (SSL Termination)**
	- L7: LB에서 한 번만 복호화 → 백엔드는 평문 HTTP만 처리 (가벼움, 인증서도 한 곳에서 관리)
	- L4: 암호화된 패킷 통과만 시킴 → 각 백엔드가 SSL 처리 → 부담 N배
2. **경로별 라우팅** — `/static/*` → Nginx 직접 응답, `/api/*` → 앱 서버. L4는 URL 못 봄.
3. **쿠키 기반 세션 고정 (Sticky Session)** — L7은 쿠키로, L4는 IP로만 가능 (같은 NAT 뒤 사용자가 한 서버로 몰림).
4. **WAF, Rate Limiting, 헤더 조작** — HTTP 내용을 봐야 가능.
5. **HTTP 단위 로깅/모니터링** — URL별 응답시간, 5xx 비율 등.

##### L4가 적합한 경우

| 케이스 | 이유 |
| --- | --- |
| DB 로드밸런싱 (MySQL, Redis) | HTTP가 아닌 TCP 프로토콜 |
| 게임 서버 (실시간 TCP/UDP) | 초저지연, HTTP 아님 |
| HTTPS E2E 암호화 강제 | 중간에서 복호화 불가 |
| 초대용량 트래픽 1차 분산 | L4가 압도적으로 빠름 (수백만 conn/sec) |

> [!example] 실무 대형 구조 — L4 + L7 조합
> ```
> [사용자] → [L4 LB: 초고속 분산] → [L7 LB: SSL/라우팅/WAF] → [앱 서버]
>            (AWS NLB 등)            (Nginx, ALB 등)
> ```

### 헬스 체크 · 하트비트

- **헬스 체크 (Health Check)** — LB가 백엔드에 주기적으로 ping/HTTP 요청을 보내 살아있는지 확인. 죽은 서버는 풀에서 제외.
- **하트비트 (Heartbeat)** — 노드들이 서로 "나 살아있다" 신호를 주기적으로 보내는 메커니즘. 주로 액티브/스탠바이 장애 감지에 사용.

### 로드 밸런싱 알고리즘

| 알고리즘 | 동작 |
| --- | --- |
| 라운드 로빈 | 서버에 순서대로 차례차례 분배 |
| 최소 연결 (Least Connections) | 현재 연결 수가 가장 적은 서버에 분배 |
| 가중치 라운드 로빈 | 서버 성능에 따라 가중치를 두고 순환 분배 |
| 가중치 최소 연결 | 가중치 + 최소 연결을 같이 고려 |

#### 🔍 최소 연결 — 어떻게 연결 수를 파악하나?

LB는 **자신을 거쳐가는 연결의 흐름을 모두 알기 때문에** 내부 카운터로 직접 추적.

```
클라이언트 ──► [로드밸런서] ──► 백엔드 서버
              (모든 연결이 여기를 통과)
```

##### L4 (TCP 기준) 동작

| 서버 | 현재 연결 수 |
| --- | --- |
| Server A | 12 |
| Server B | 8 ← 선택됨 |
| Server C | 15 |

- TCP **SYN** 도착 → 가장 적은 서버 선택, 카운터 `+1`
- TCP **FIN/RST** 또는 종료 감지 → 카운터 `-1`
- 비정상 종료 대비 **idle timeout**으로도 감소

##### L7 (HTTP 기준) 동작 — 활성 요청 수 (active requests)

HTTP/1.1 Keep-Alive로 한 연결에 여러 요청이 흐름:

```
[TCP 연결 1개]
   ├─ GET /a
   ├─ GET /b
   └─ GET /c
```

- L4: 연결 1개로 셈
- L7: **처리 중인 요청 수 (in-flight)** 로 셈
- HTTP/2, HTTP/3는 한 연결에서 여러 **스트림(stream)** 이 병렬로 흐르므로 스트림 단위 카운트

**카운팅 시점:**

```
요청 도착 → 백엔드 선택 → counter += 1
              │
              ├─ 백엔드로 전달
              ├─ 응답 수신
              └─ 클라이언트로 응답 완료 → counter -= 1
```

##### Power of Two Choices (P2C)

서버 N대 매번 비교는 O(N) → 느림. 실제 구현:

1. 랜덤 2개 뽑음
2. 둘 중 적은 쪽 선택

> [!tip]
> 이 단순한 방법이 거의 최적에 가까움 (수학적으로 증명).
> Nginx / Envoy / HAProxy 모두 이 변형 사용.

##### 가중치 결합 — Weighted Least Request

$$\text{score} = \frac{\text{active\_requests}}{\text{weight}}$$

| 서버 | 활성 요청 | 가중치 | 점수 |
| --- | --- | --- | --- |
| A | 10 | 1 | 10 |
| B | 15 | 5 | **3 ← 선택** (점수 낮음 = 여유) |

##### 함정 4가지

> [!warning] 최소 연결의 함정
> 1. **연결 수 ≠ 실제 부하** (CPU/메모리). 보완: 에이전트 기반 LB (F5 BIG-IP Dynamic Ratio)에서 서버가 자기 부하를 LB에 보고.
> 2. **롱폴링 / SSE / WebSocket** — 한 요청이 수십 분 유지되면 카운터가 안 떨어짐 → 별도 풀로 분리하거나 라운드로빈.
> 3. **신규 서버 콜드 스타트 (Thundering Herd)** — 활성 요청 0 → 모든 트래픽 몰림 → 다운. **Slow start mode**로 점진 가중치 증가 (예: 30초 10%, 1분 50%, 2분 100%).
> 4. **분산 LB 간 시야 불일치** — LB 여러 대일 때 각자 자기 카운터만 봄. P2C가 이 불일치에 강건한 이유.

#### 🛠️ 실무 도구

| 도구 | 특징 | 주 용도 |
| --- | --- | --- |
| **Nginx** | 가장 대중적. 웹 서버 + 리버스 프록시 겸용 | 대부분의 웹사이트 |
| **HAProxy** | 로드밸런싱 전문. 매우 빠름 | 대규모 트래픽 분산 |
| **Envoy** | 최신. 마이크로서비스/쿠버네티스용 | MSA, 서비스 메시 |

> [!example] Nginx 설정 — `least_conn` 디렉티브
> ```nginx
> upstream backend {
>     least_conn;
>     server app1:8080;
>     server app2:8080;
> }
> ```

- **Envoy** — `LEAST_REQUEST` 정책. 기본이 P2C, `choice_count`로 샘플 수 조절.
- **HAProxy** — `balance leastconn`.

---

## 🌐 포워드 프록시 · 리버스 프록시

### 오리진 서버 · 중간 서버 · 클라이언트

- **클라이언트** — 요청을 보내는 쪽.
- **오리진 서버 (Origin Server)** — 실제 리소스를 가진 최종 서버.
- **중간 서버 (Intermediary)** — 클라이언트와 오리진 사이에 위치. 캐싱, 보안, 로드 밸런싱 수행.

### 다중화된 오리진 서버

오리진을 여러 대로 두고 리버스 프록시가 분산 → 가용성·확장성 확보.

### 인바운드 · 아웃바운드

- **인바운드 (Inbound)** — 외부 → 내부 방향으로 들어오는 트래픽.
- **아웃바운드 (Outbound)** — 내부 → 외부로 나가는 트래픽.

### HTTP 중간 서버: 프록시 vs 게이트웨이

| 구분 | 위치 | 클라이언트 인식 |
| --- | --- | --- |
| **프록시 (Proxy)** | 클라이언트 쪽 대리인 | "프록시를 통해 보낸다"는 걸 인식 |
| **게이트웨이 (Gateway)** | 서버 쪽 대리인 | 게이트웨이를 그냥 최종 서버로 인식 |

### 포워드 프록시 / 리버스 프록시

> [!note] 포워드 프록시 = 프록시
> - **위치**: 클라이언트 앞단
> - **용도**: 사내 인터넷 접근 제어, 익명성 확보, 캐싱

> [!note] 리버스 프록시 = 게이트웨이
> - **위치**: 오리진 서버 앞단
> - **용도**: 로드 밸런싱, 캐싱(CDN), SSL 종료, 보안(WAF)
> - **예**: Nginx, HAProxy, CloudFront

---

## 🚀 실무 흐름: 서비스 성장에 따른 구조 진화

### Stage 1 — 서비스 오픈 (사용자 100명)

```
[사용자] ──► [서버 1대]
```

- LB 없음. **SPOF 존재.**

### Stage 2 — 트래픽 증가 (사용자 1만명)

```
[사용자] → [Nginx 리버스 프록시] → [앱 서버 1/2/3]
```

```nginx
upstream app_servers {
    least_conn;
    server app1.internal:8080;
    server app2.internal:8080;
    server app3.internal:8080;
}
server {
    listen 443 ssl;
    server_name example.com;
    location / { proxy_pass http://app_servers; }
}
```

- ✅ 로드 밸런싱, SSL 종료, 헬스 체크
- ⚠️ Nginx 자체가 SPOF

### Stage 3 — 고가용성 확보 (사용자 10만명)

```
              [DNS]
                │
        ┌───────┴───────┐
     [Nginx-1]      [Nginx-2]   (액티브/액티브, 하트비트 감시)
        │               │
        └───┬───────┬───┘
            ▼       ▼
       [앱서버 1/2/3]
            │
       [DB Primary] → [DB Replica]
```

- Nginx 이중화
- DB Primary/Replica로 읽기/쓰기 분산

### Stage 4 — L7 라우팅 (마이크로서비스 전환)

```
            [Nginx L7]
       /         |         \
 /api/order/* /api/product/* /api/user/*
      ▼         ▼            ▼
   [Order]   [Product×5]   [User×2]
```

```nginx
location /api/order/   { proxy_pass http://order_servers; }
location /api/product/ { proxy_pass http://product_servers; }
```

가중치로 고성능 서버에 트래픽 더 몰기:

```nginx
upstream product_servers {
    server prod1:8080 weight=1;
    server prod2:8080 weight=3;
    server prod3:8080 weight=3;
}
```

### Stage 5 — 글로벌 + CDN (사용자 100만명)

```
[전 세계 사용자]
       │
[CloudFront/CDN]        ← 리버스 프록시 + 캐싱
       │ (캐시 미스만)
[AWS ALB]               ← 관리형 L7 LB
       │
[ECS/Kubernetes 클러스터]
       ├─ [Envoy 사이드카] → Order Pod × N
       ├─ [Envoy 사이드카] → Product Pod × N
       └─ [Envoy 사이드카] → User Pod × N
              (서비스 메시)
```

- **CDN** — 글로벌 리버스 프록시 + 캐시. 사용자와 가까운 곳에서 응답.
- **ALB** — AWS 관리형 L7 LB.
- **Envoy 사이드카** — 각 Pod 옆에 붙는 미니 프록시. 서비스 간 통신을 가로채 로드밸런싱/재시도/모니터링.
- **Kubernetes** — Pod 오토스케일링 → **Slow start**로 신규 Pod 보호.

### 단계별 요약

| 규모 | 구조 | 핵심 기술 |
| --- | --- | --- |
| 소형 | 단일 서버 | — |
| 중형 | LB 1대 + 앱 N대 | 리버스 프록시, 헬스체크 |
| 대형 | LB 이중화 + DB 이중화 | 고가용성, 하트비트 |
| MSA | L7 라우팅 | URL/도메인 기반 분기 |
| 글로벌 | CDN + 관리형 LB + 서비스 메시 | 캐싱, 사이드카 |

---

## 💬 면접/실무 자주 묻는 포인트

> [!question] Q1. 왜 Nginx를 앞단에 두나요?
> SSL 종료, 로드밸런싱, 정적 파일 캐싱, 보안(WAF), 백엔드 보호.

> [!question] Q2. L4 vs L7 언제 쓰나요?
> DB·단순 TCP는 L4. HTTP API는 L7. HTTPS면 모놀리식이어도 L7.

> [!question] Q3. 서버 한 대 추가하면 끝인가요?
> 아님. **Slow start**로 천천히 트래픽 받게 해야 함. 안 그러면 thundering herd.

> [!question] Q4. DB는 어떻게 로드 밸런싱?
> 읽기/쓰기 분리 (Primary-Replica). 또는 샤딩.

> [!question] Q5. 세션 유지를 어떻게?
> Sticky Session (L7 쿠키 기반) 또는 외부 세션 스토어(Redis)로 모든 서버가 공유.

---

## 🔭 더 깊게 파보면 좋을 포인트

### 로드 밸런싱 / 프록시 심화

- [ ] **Consistent Hashing** — 캐시 서버 분산 시 노드 추가/제거에도 키 재배치 최소화. Memcached, Redis Cluster, CDN에 필수.
- [ ] **Sticky Session vs Stateless 세션** — 쿠키 기반 sticky의 한계와 JWT/Redis 세션 스토어 비교.
- [ ] **gRPC 로드 밸런싱** — HTTP/2 멀티플렉싱 때문에 L4 LB로는 불균형. 클라이언트 사이드 LB나 Envoy 필요한 이유.
- [ ] **TLS 종료 vs Passthrough vs Re-encrypt** — 보안 요구사항별 SSL 처리 전략.
- [ ] **WAF (Web Application Firewall)** — ModSecurity, AWS WAF, Cloudflare. OWASP Top 10 차단 규칙.
- [ ] **Rate Limiting 알고리즘** — Token Bucket, Leaky Bucket, Sliding Window.

### 고가용성 / 장애 복구

- [ ] **페일오버 메커니즘** — VIP + Keepalived (VRRP), DNS Failover, AWS Route 53 Health Check.
- [ ] **Circuit Breaker 패턴** — 장애 전파 차단 (Hystrix, Resilience4j, Envoy outlier detection).
- [ ] **Bulkhead 패턴** — 한 영역의 장애가 다른 영역으로 번지지 않게 격리.
- [ ] **카오스 엔지니어링** — Netflix Chaos Monkey처럼 일부러 장애 일으켜 복원력 검증.
- [ ] **SLA / SLO / SLI** — 가용성 목표 수치화와 에러 버짓 관리.

### 데이터 계층

- [ ] **DB Replication** — 동기 vs 비동기 복제. Replica Lag 문제.
- [ ] **Read/Write Splitting** — 애플리케이션 레벨 vs ProxySQL/PgBouncer 활용.
- [ ] **샤딩 (Sharding)** — 수평 분할 전략과 리샤딩 비용.
- [ ] **CAP 이론과 PACELC** — 분산 시스템의 일관성/가용성 트레이드오프.

### 트래픽 분산 / 글로벌

- [ ] **CDN 내부 동작** — Edge → Regional → Origin 계층. Cache-Control, ETag, Stale-While-Revalidate.
- [ ] **GSLB (Global Server Load Balancing)** — GeoDNS, Anycast로 지역별 라우팅.
- [ ] **Anycast vs Unicast** — 같은 IP를 여러 곳에 두는 트릭. CDN, DNS 루트 서버.

### 클라우드 / 컨테이너 환경

- [ ] **Service Mesh 심화** — Istio, Linkerd. 사이드카 패턴의 장단점.
- [ ] **API Gateway vs 리버스 프록시** — Kong, AWS API Gateway. 인증/요금/변환 기능.
- [ ] **오토스케일링 전략** — CPU/메모리 기반 vs RPS 기반. Predictive Scaling.
- [ ] **Kubernetes Ingress vs Service** — ClusterIP, NodePort, LoadBalancer, Ingress 차이.

### 관측 가능성 (Observability)

- [ ] **로깅/메트릭/트레이싱 3축** — ELK, Prometheus + Grafana, Jaeger/OpenTelemetry.
- [ ] **분산 트레이싱** — 마이크로서비스 간 요청 흐름 추적. Trace ID 전파.

### 보안

- [ ] **DDoS 방어** — L3/L4/L7별 공격 유형과 방어 (Cloudflare, AWS Shield).
- [ ] **mTLS (Mutual TLS)** — 서비스 간 양방향 인증. Service Mesh에서 기본.
- [ ] **Zero Trust 네트워크** — BeyondCorp 모델.

---

## 🔗 관련 노트

- [[Chapter 4-2 TCP와 UDP]]
- [[Chapter 5-2 HTTP]]
- [[Chapter 5-3 HTTP 헤더와 HTTP 기반 기술]]
- [[CORS]]
