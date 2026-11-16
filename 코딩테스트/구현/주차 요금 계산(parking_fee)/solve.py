'''
기본시간(분), 기본요금, 단위 시간(분), 단위 요금 : 각각 정수로 주어진 배열 fees
"hh:mm 차량번호 입/출차" 형태의 문자열이 시간순으로 오름차순 정렬된 문자열 배열 records

차량번호가 작은 자동차부터 청구할 주차요금을 정수배열에 담아 반환
---------------------------

입차후 출차기록이 없는 차는 23:59에 출차한 것으로 간주

알아내야할 정보
1. 각 차량이 00시 부터 23:59 몇분동안 주차장에 있었는지 정보

각 차량별 머문 시간(분)이 구해지면
{차량번호:머문시간(분)} -> 차량번호 오름차순 정렬

이걸 구하려면
record  출차시간-입차시간을 해야함

{차량번호:[(입차시간,출차시간)]} -> 수정
차량 번호 별로 (입차시간,출차시간)을 꺼내서 계산

-----------------------------------

힌트를 받아서 저장하려는 자료형을 수정함
주차중인 차량만 자료형에 저장하는 방식으로
IN을 만나면 inPark = {차량번호:입차시간을} 저장해뒀다 OUT을 만나면 해당하는 차량의 입차시간과 출차시간을 빼서 주차장에 머무른 시간을 갱신하고
del inPark[차량번호] 로 제거

마지막에 inPark의 길이가 1 이상이면 입차후 23:59에 일괄 출차한 차들이니 별도로 머무른 시간 갱신

입출차 시각 문자열의 경우
[:2] 시간을 분으로 *60

[3:] 거기다 분을 더해 출차시간-입차시간

(입차시간) 즉 출차 시간이 없는 경우 23:59 에다가 빼기


2. 차량별 청구요금

기본시간 으로 빼서 0이하면 기본요금만 청구
0 초과면 단위시간(분)으로 나눠 올림해 단위 요금을 곱한다.



'''
import math
def solution(fees, records):
    # 차량별 주차 시간(분) 을 저장
    carParkminute = {}
    # 주차중 = {차량번호: 입차시각(분)}
    inPark = {}

    # {차량번호:[(입차시간,출차시간)]} 만들기
    for info in records:
        t, n, io = info.split(" ")
        # 입차 시간 기록
        if io == "IN":
            inPark[n] = int(t[0:2])*60+int(t[3:])
        else:
            # 출차니깐 inPark에서 차량을 꺼내 시간 계산
            outTime = int(t[0:2])*60+int(t[3:])
            inTime = inPark[n]

            if n in carParkminute: # 이미 입출차 기록이 있으면 거기다 누적
                carParkminute[n]+= (outTime-inTime)
            else:
                carParkminute[n] = (outTime-inTime)

            # 출차 했으니 제거
            del inPark[n]
    # 입차는 했으나 출차한 기록이 없는경우
    if len(inPark) >= 1:
        outTime = 23*60+59
        for carNumber, inTime in inPark.items():
            if carNumber in carParkminute:
                carParkminute[carNumber]+= outTime-inTime
            else:
                carParkminute[carNumber] = outTime-inTime

    # 이제 주차요금 정산 시작
    # 우선 차량 번호 작은 순으로 정렬
    result = []
    carParkminute = sorted(carParkminute.items(), key=lambda x:x[0])
    for _,t in carParkminute:
        # 기본시간 내로 머물렀다면
        if fees[0]>=t:
            result.append(fees[1])
        else:
            money= fees[1]+(math.ceil((t-fees[0])/fees[2]))*fees[3]
            result.append(money)


    return result
