
# TCP 통신 단계와 세그먼트 구조<br>
TCP는 크게 세 단계로 나뉨: 연결 수립, 데이터 송수신, 연결 종료 <br>
MSS(Maximum Segmant Size): TCP로 전송할 수 있는 최대 페이로드 크기를 의미, MSS를 고려할 때 TCP 헤더의 크기는 제외한다.<br>
MTU(Maximum Transmission Unit) = 최대 전송단위는 포함한다.<br>
헤더구조는 아래와 같다.
1. 송신지 포트, 수신지 포트: 송신지 또는 수신지 애플리케이션을 식별
2. 순서번호: 송신되는 세그먼트의 올바른 순서를 보장, 세그먼트 데이터의 첫 바이트에 부여
3. 확인 응답 번호: 상대 호스트가 보낸 세그먼트에 대한 응답. 다음으로 수신하기를 기대하는 순서번호가 명시
4. 제어 비트: 플래그 비트라 부름. 현재 세그먼트에 대한 부가 정보 나타냄
5. 윈도우: 수신 윈도우의 크기 명시됨(한번에 수신하고자 하는 데이터의 양)

그외 더있으나  핵심만 추림
# TCP 연결 수립과 종료

- Three-Way-Hand shake: syn, syn+ack, ack, 액티브 오픈, 패시브 오픈

- Four-Way-Hand shake: fin, ack, 액티브 클로즈, 패시브 클로즈
# TCP 상태

- stateful protocol
- 주요 상태
	- closed, listen
	- syn-sent,syn-received,established
	- fin-wait-1,close-wait,fin-wait-2,last-ack,time-wait,closing

# UDP 데이터 그램 구조

- stateless protocol
- 송신지, 수신지 포트, udp 길이, 체크섬 필드
