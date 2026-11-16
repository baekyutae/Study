'''
주차 요금을 나타내는 정수 배열 fees : 기본시간(분), 기본요금, 단위시간(분), 단위 요금
자동차들의 입출차 내역을 나타낸 문자열 배열 records: "시각 차량번호 입/출차" (시간 기준 오름차순 정렬되어 있음)
차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

알아야 하는 정보
pTime = {차량번호:주차시간(분)}

주차시간 어케 구함?
입차중인 차:입차시간 를 저장하는 current = {차량번호:입차시간(분)}
record에서 각 원소를 split
IN이면 current에 저장
OUT이면 출차시간-입차시간해서 pTime[차량번호]에 누적
del current[차량번호]

records에서 모든 기록을 다 훑은후 len(current)이 >=1 이라면 -> 23:59에 출차한 차량
23:59-입차시간해서 pTime[차량번호]에 누적

pTime 을 차량번호 순으로 정렬해
각 주차시간 마다 기본요금 + max(0,math.ceil((주차시간-기본시간)/단위시간)*단위요금)
해서 result = []에 저장

-------
시간복잡도
1. for info in records 에서 records의 길이 n 에다가 매번 문자열 슬라이싱 4 -> 4n
2. 출차하지 않은 차에 대한 for문: 최대 n
3. 각 차량의 주차시간으로 가격 정산 for문: n -> records의 최대 길이 1000을 넘을수 없다 그래서 최대n
왜? 예를들어 차량이 1001대라면 한대는 무조건 입차를 못하게됨

o(n)

공간복잡도
pTime : n
current: n
o(n)

------------

edge case
1. 입차후 출차 기록이 없는경우: if len(current)>=1: 여기에서 처리

'''
from collections import defaultdict
import math

def solution(fees, records):
    pTime = defaultdict(int)
    current = {}
    for info in records:
        t, c, io = info.split(" ")
        if io == "IN":
            current[c] = int(t[:2])*60+int(t[3:])
        else:
            oTime = int(t[:2])*60+int(t[3:])
            iTime = current[c]

            pTime[c] += oTime-iTime

            del current[c]
    if len(current)>=1:
        for c,t in current.items():
            oTime = 23*60+59
            iTime = t
            pTime[c] += oTime-iTime
    result = []
    for _,t in sorted(pTime.items(), key= lambda x:int(x[0])):
        value = fees[1] + max(0,math.ceil((t-fees[0])/fees[2])*fees[3])
        result.append(value)

    return result
