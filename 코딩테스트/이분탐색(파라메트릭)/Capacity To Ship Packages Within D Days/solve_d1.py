class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def carryDay(c):
            day = 1
            remain = c
            for weight in weights:
                remain -= weight
                if remain < 0:
                    day += 1
                    remain = c
                    remain -= weight

            return day

        lo, hi = max(weights), sum(weights)

        # 이분 탐색
        while lo<hi:
            mid = (lo+hi)//2
            if carryDay(mid) <= days:
                hi = mid
            else:
                lo = mid+1

        return lo
