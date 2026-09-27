from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speedCheck(speed):
            # pile이 3이고 speed가 7 이라도 한시간 동안 해당 더미에 있어야 하므로
            # 음수로 만들어 나누어 -0.4285..... -> -1 -> 1
            return sum(-(-(pile) // speed) for pile in piles)

        # 이분 탐색 시작 범위
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2

            if speedCheck(mid) <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
