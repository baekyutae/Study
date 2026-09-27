'''
koko가 경비원이 h시간 내로 돌아오기전에 piles 내에 바나나를 다 먹어치우려함
시간당 섭취량중 최솟값을 반환

최솟값을 구해야하고, 최소값을 파라미터로 대입 했을 때 참거짓 판별이 가능, 대입한 파라미터보다 크거나 작은값으로 조건 충족 여부도 확인 가능
-> 파라매트릭 서치


시간복잡도는
1. while 문반복: log(max(piles)-1)
2. 매번 eatTime에서 for문 반복 len(piles) 을 n이라 할때

o(nlog(max(piles)-1))

최악의 경우 n은 1만 * log10억 이면 약 29 대략 29만이니 시간 초과 걱정없음

공간복잡도
o(1)
'''

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        def eatTime(t):
            # 시간당 t 만큼 먹을 때
            # 다먹을 때 까지 걸리는 시간 반환

            count = 0
            for pile in piles:
                if pile%t != 0:
                    count += (pile//t+1)
                else:
                    count += (pile//t)

            return count

        lo, hi = 1, max(piles)

        while lo<hi:
            mid = (lo+hi)//2

            if eatTime(mid) <= h:
                # 시간내로 다먹을 수 있으면 더 적게 먹어도 가능한지 확인
                hi = mid

            else:
                lo = mid+1

        return lo
