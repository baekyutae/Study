# CORS(Cross-Origin Resource Sharing) 란?

서버가 브라우저에게 "나와 다른 출처(도메인, 포트, 프로토콜)의 웹 페이지에서도 내 리소스를 불러와도 괜찮아"라고 허락해 주는 HTTP 헤더 기반 메커니즘

브라우저는 보안을 위해 기본적으로 다른 도메인으로의 요청을 막는다. 프론트엔드(`domain-a.com`)에서 백엔드 API(`domain-b.com`)로 `fetch()`나 `axios` 요청을 보낼 때 이 차단을 풀기 위해 서버 측에서 올바른 CORS 헤더를 내려주어야 한다.


# Preflight (사전 요청)

CORS 요청은 크게 '단순 요청(Simple Request)'과 '사전 요청(Preflighted Request)'으로 나뉜다.

preflight란?
브라우저가 본 요청(예: `POST`, `PUT`)을 보내기 전에, 서버에 **`OPTIONS` 메서드**를 사용하여 "이 요청을 보내도 안전한가요?"라고 미리 확인해 보는 과정

**언제 발생하는가?**

- `GET`, `POST`, `HEAD` 이외의 메서드를 사용할 때
    
- `Content-Type`이 `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`이 **아닐 때**. (즉, API 통신에 가장 많이 쓰는 `application/json`은 무조건 Preflight를 발생시킴.)
    
- 커스텀 헤더(예: `Authorization` 토큰, `X-PINGOTHER` 등)를 포함할 때


# 서버 측에서 세팅해야 할 핵심 응답 헤더 4가지

Preflight 요청(`OPTIONS`)을 받은 백엔드 서버는 다음 헤더들을 응답에 포함해 브라우저의 CORS 검증(Validation) 알고리즘을 통과할 수 있도록 Access-Control 헤더를 발급해 준다.

1. `Access-Control-Allow-Origin
   **역할:** 리소스 접근을 허용할 특정 출처(Origin)를 지정
   
   특징: `https://domain-a.com`처럼 특정 도메인을 명확하게 명시하거나, `*`를 지정하여 모든 도메인의 접근을 허용할 수 있다. 단 쿠키나 인증 헤더 등 자격 증명(Credentials)이 포함된 요청에서는 보안상 `*`를 사용할 수 없으며, 반드시 정확한 출처를 명시해야 한다.

2. `Access-Control-Allow-Methods`
   **역할**: 클라이언트가 실제 본 요청(Actual Request)에서 사용할 수 있도록 허용된 HTTP 메서드 목록을 지정.
   
   **특징:** 클라이언트가 사전 요청 시 `Access-Control-Request-Method` 헤더를 통해 사용할 메서드를 물어보면, 서버는 이에 대한 응답으로 `GET, POST, PUT, DELETE, OPTIONS` 등 허용하는 메서드들을 쉼표(,)로 구분하여 반환해 준다.
   
3. `Access-Control-Allow-Headers`
   **역할:** 클라이언트가 실제 본 요청 시 사용할 수 있도록 허용된 HTTP 커스텀 헤더 목록을 지정한다.
   
   특징: 프론트엔드에서 `Authorization` (토큰)이나 명시적인 `Content-Type` 등 기본적으로는 차단되는 헤더를 포함해 전송하려 할 때, 서버가 이를 받아들일지 결정한다. 예: `Content-Type, Authorization, X-Requested-With`

4. `Access-Control-Max-Age`
   
   **역할:** 브라우저가 Preflight 요청의 성공적인 확인 결과를 캐시(Cache)해 둘 수 있는 시간을 초(second) 단위로 지정.
   
   **특징:** `OPTIONS` 요청을 매번 보내게 되면 불필요한 네트워크 지연과 서버 부하가 발생한다. 때문에 이 헤더에 지정된 시간(예: `86400` = 24시간) 동안 브라우저는 캐시된 결과를 믿고 사전 요청을 생략한 채 곧바로 본 요청을 보내게 된다.