'''
화물의 무게를 나타낸 배열 weights이 있을때 days일 이내에 운송할수 있는 배의 최소 적재 용량을 구해라

최소값을 찾아야함 -> 용량을 변수로 두고 걸리는 날짜를 구함 -> days 이내면 더 용량을 줄여보고 days를 초과하면 늘려보고
-> 파라매트릭 서치로 접근

시간복잡도
1. while 문 log(sum(weights) - max(weights))
2. for문 weights의 길이 n

o(nlog(sum(weights) - max(weights)))

공간복잡도
o(1)

'''
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def carryDays(tone):
            # 수송량이 tone일때 모든 weights의 화물을 옮기는데 걸리는 날짜 반환
            remain = tone
            day = 1
            for weight in weights:
                if remain < weight:
                    day+=1
                    remain = tone
                    remain -= weight
                else:
                    remain -= weight
            
            return day

        # 탐색 범위 설정
        lo, hi = max(weights), sum(weights) # 최소값의 경우 가장 무거운 화물까지 수송가능 해야 하며, 최대값의 경우 하루만에 모든 화물을 다 실어 나를 수 있음

        while lo<hi:
            mid = (lo+hi)//2
            if carryDays(mid) <= days:
                hi = mid

            else:
                lo = mid+1

        return lo
