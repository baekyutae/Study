'''
풀이: 파라메트릭 서치 (건너는 사람 수 m을 이분탐색)
- 사람은 가장 가까운, 0이 아닌 돌을 밟으므로 한 사람이 건너면 0이 아닌 돌은 전부 1씩 줄어든다
- 그래서 m번째 사람 차례에 0인 돌 = 원래 값이 m보다 작은 돌
- 0인 돌이 k개 연속이면 k+1칸을 뛰어야 해서 못 건넌다
- m명이 건너면 m-1명도 건너므로(단조성) 가장 큰 m을 이분탐색으로 찾는다
- 상한 max(stones): k ≤ 돌 개수라서 돌이 전부 0이 되면 못 건넌다
- 시간 복잡도: O(돌 개수 × log(돌 값의 최댓값))
'''


def solution(stones, k):
    def can_cross(m):
        run = 0                 # 지금까지 연속으로 m보다 작은(= 0이 된) 돌의 개수
        for s in stones:
            if s < m:
                run += 1
                if run >= k:    # k개 연속으로 0이면 뛰어넘을 수 없음
                    return False
            else:
                run = 0
        return True

    lo, hi, answer = 1, max(stones), 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if can_cross(mid):      # mid명이 건널 수 있으면 더 많은 인원을 시도
            answer, lo = mid, mid + 1
        else:                   # 못 건너면 인원을 줄임
            hi = mid - 1
    return answer
