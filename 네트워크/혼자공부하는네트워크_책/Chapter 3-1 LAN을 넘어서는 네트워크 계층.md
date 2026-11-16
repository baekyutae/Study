# 데이터 링크 계층의 한계

1. 물리계층과 데이트 링크 계층만으론 다른 네트워크 까지의 도달경로를 파악하기 어려움
2. mac 주소만으로는 모든 네트워크에 속한 호스트의 위치를 특정하기 어려움
   
ip주소, DHCP


# 인터넷 프로토콜


IP주소 형태, 옥텟

IP의 기능: IP 주소지정, IP 단편화

RFC(Request From Comments) 문서

### IPv4

프레임 헤더, 프레임 페이로드, ipv4 패킷헤더, ipv4 패킷 페이로드

ipv4 패킷헤더: 식별자, 플래그(df,mf), fragment offset, ttl, protocol, 송신지 ip주소와 수신지 ip주소

### IPv6

ipv6 패킷헤더: 다음헤더(기본헤더/확장헤더)

확장헤더: 홉 간 옵션, 수신지 옵션, 라우팅, esp(encapsulating security payload), ah(authentication header)

ipv6의 단편화: 단편화 확장 오프셋, m플래그, 식별자 필드

홉 제한

송신지 ip주소와 수신지 주소

# ARP

Adress Resolution Protocol

arp 요청, arp 응답, arp 테이블 갱신

arp 패킷

동일한 네트워크가 아닌 호스트간 arp

IP단편화를 피하는 방법: 경로 MTU