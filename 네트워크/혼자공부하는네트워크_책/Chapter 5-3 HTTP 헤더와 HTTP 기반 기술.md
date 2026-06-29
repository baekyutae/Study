


# HTTP 헤더

- 요청시 활용되는 HTTP 헤더: HOST, User-Agent, Referer, Authorization

authorization 요새는 basic 타입 말고 bearer 타입 씀

- 응답시 활용되는 http 헤더: server, allow, Retry-After, Location, WWW-Authenticate
  
  WWW-Authenticate: realm이란

- 응답과 요청 모두에서 활용 되는 http 헤더: Date, Connection, Content-Length, Content-Type, Content-Language, Content-Encoding

# 캐시

개인 전용 캐시, 공용캐시, 원본이 아닌 사본 저장, Cache freshness

캐시된 데이터의 유효기간 설정 방법 :expire header, cache-control header

캐시 신선도 검사: 
1. 날짜 기반: If-Modified-Since, 200 / 304 status code(not modified), Last-modified  
2. 엔티티 태그: Version, If-None-Match

# 쿠키

http 특성 보완(stateless)
세션인증, 세션 id

set-cookie header, cookie header
domain 속성

secure, http only 속성

#  콘텐츠 협상과 표현


content negotiation
representation:송수신 가능한 자원의 형태

get method: 자원의 특정 표현을 습득하기 위한 메서드

accept language header, accept-charset, accept-encoding

선호도(우선순위) q