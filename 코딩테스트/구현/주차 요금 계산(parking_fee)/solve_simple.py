# 해설의 간단한 풀이: 주차중 딕셔너리 + defaultdict 누적, pop으로 꺼내며 삭제
from collections import defaultdict
import math

def solution(fees, records):
    base_min, base_fee, unit_min, unit_fee = fees
    parking = {}                      # 차량 → 입차 시각(분)
    total = defaultdict(int)          # 차량 → 누적 주차 분

    for rec in records:
        t, car, io = rec.split()
        minute = int(t[:2]) * 60 + int(t[3:])
        if io == "IN":
            parking[car] = minute
        else:
            total[car] += minute - parking.pop(car)

    for car, in_minute in parking.items():   # 출차 기록 없는 차
        total[car] += 23 * 60 + 59 - in_minute

    return [base_fee + max(0, math.ceil((total[c] - base_min) / unit_min)) * unit_fee
            for c in sorted(total)]
