from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speedCheck(speed):
            result = 0
            for pile in piles:
                result += -(-(pile) // speed)

            return result

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if speedCheck(mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
