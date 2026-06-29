# http의 특성

## 요청-응답 기반 프로토콜

- 클라이언트와 서버
## 미디어 독립적 프로토콜

- mime 타입, 미디어 타입, 서브타입

## stateless protocol

- 확장성과 견고성
## 지속연결 프로토콜


# http 메세지 구조

- 시작 라인, 필드라인, 메세지 본문
- http 버전, status code, reason phase
- http 헤더

# http 메서드

get, head, post, put, patch, delete, connect, options, trace

# http 상태 코드(status code)

- 200번대 성공 코드: 200,  201, 202, 204
- 300번대 리다이렉션 상태 코드
	  영구적: 301, 308
	  일시적: 302,303,307

- 400번대 클라이언트 에러 상태 코드: 400, 401, 403, 404, 405
- 500번대 서버 에러 상태 코드: 500, 502, 503