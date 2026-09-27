'''
풀이 2: answer 변수 없이 lo를 답으로 반환 (lo < hi)
- 가장 큰 값을 찾으므로 참이면 lo = mid (mid를 남김), 거짓이면 hi = mid - 1
- lo = mid를 쓰면 mid는 올림 (lo + hi + 1) // 2
  내림이면 hi와 lo가 1 차이일 때 mid == lo가 되어 범위가 줄지 않고 무한 반복
'''


def solution(stones, k):
    # m번째 사람이 개울을 건널수 있는지 여부로 이분 탐색

    def canCross(m):
        run = 0
        for stone in stones:
            if stone < m:
                run += 1
                if run >= k:
                    return False
            else:
                run = 0
        return True

    lo, hi = 1, max(stones)
    while lo < hi:
        mid = (lo + hi + 1) // 2

        if canCross(mid):
            lo = mid

        else:
            hi = mid - 1

    return lo
