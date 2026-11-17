'''
1. 문제파악

주차 요금을 나타내는 정수 배열 fees, 자동차의 입/출차 내역을 나타내는 문자열 배열 records가 매개변수로 주어짐
입차후 나가지 않은 차는 23:59에 나간걸로 간주

차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수

records의 각 원소는 "시각 차량번호 내역(IN/OUT)" 형식의 문자열
records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어짐

-> 주어진 단서(fees,records)를 알맞게 가공하여, 요구하는 답을 도출하는 함수 구현 => 구현문제

각차량별 주차시간(분)을 구해야함


2. 엣지 케이스
입차후 출차가 없는경우: if len(parking) >=1 로 처리


3. 복잡도
시간복잡도
- for info in records: records의 길이 n만큼 비용듬
- for문안에 시간 문자열 슬라이싱: 길이가 5이므로 항상 5만큼 비용듬 
- if len(parking) >=1: 출차를 안한경우 최악의 경우 n만큼 비용듬
- 차량 비용계산: 차량 댓수는 최대 records의 길이 n

o(n)

공간복잡도
parking = {}: 최대 n
parkTime = defaultdict(int): 최대 n
o(n)
'''
# 로직 설계
'''
import math
def solution(fees, records):
    # 차량별 주차 시간 저장 
    # parkTime = {(차량번호:주차시간}
    parkTime = {}

    records에서 파싱
        t, n, i_o
    만약 i_o == "IN" 이면 park에 기록
    parking : 입차해있는 차들 저장 리스트 {차번호:입차시간(분단위)} -> 계산 편의를 위해 시간은 분으로 변환해 저장

    i_o = "OUT" 이면:
        주차시간 계산해서 저장
        parkTime에 없으면 새로 생성
        있으면 시간 누적

        나갔으니 parking에서 제거
        del parking[해당차량번호] 

    records에서 다꺼냈는데 len(parking)>=1 이면?:
        23:59에 출차한걸로 간주하고 계산해서
        parkTime.append((차량번호,주차시간))

    parkTime 을 차량번호 오름차순으로 정렬

    answer = []
    차량별로 주차요금을 계산
        기본시간 초과면:
            비용 = fees[1] + math.ceil((주차시간-fees[0])/fees[2])*fees[3]
            answer.append(비용)
        초과가 아니라면
            비용 = fees[1]
            answer.append(비용)
    
    return answer
'''
# 제출 코드
import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    parkTime = defaultdict(int)
    parking = {}

    # 차량별 주차시간 계산
    for info in records:
        t, n, i_o = info.split(" ")
        if i_o == "IN":
            in_minute = int(t[:2])*60+int(t[3:])
            parking[n] = in_minute

        else:
            out_minute = int(t[:2])*60+int(t[3:])
            parkTime[n] += out_minute-parking[n]
            del parking[n]

    if len(parking) >=1:
        for number, in_minute in parking.items():
            out_minute = 1439
            parkTime[number] += out_minute-in_minute

    # parkTime 차량번호 기준 오름차순 정렬
    parkTime = sorted(parkTime.items(), key = lambda x:int(x[0]))

    # 차량별 요금 계산
    for _,t in parkTime:
        if t>fees[0]:
            fee = fees[1] + math.ceil((t-fees[0])/fees[2])*fees[3]
            answer.append(fee)
        else:
            answer.append(fees[1])


    return answer