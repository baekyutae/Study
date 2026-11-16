'''
풀이 4: 슬라이딩 윈도우 최댓값(덱), O(n)
- x명이 건널 수 있다 <=> 길이 k인 모든 구간에서 최댓값이 x 이상
- 따라서 답 = 길이 k인 구간별 최댓값 중 최솟값
- 덱에는 값이 줄어드는 순서로 위치를 저장해, 맨 앞이 항상 현재 구간의 최댓값
- 해설: 덱 풀이 해설.md
'''

from collections import deque


def solution(stones, k):
    dq = deque()                 # 값이 줄어드는 순서로 위치를 저장
    answer = float('inf')
    for i, v in enumerate(stones):
        # v 이하인 뒤쪽 값은 v보다 먼저 빠지고 v보다 크지도 않아 최댓값이 될 수 없음
        while dq and stones[dq[-1]] <= v:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:       # 구간 밖으로 나간 맨 앞 위치 제거
            dq.popleft()
        if i >= k - 1:           # 구간에 돌이 k개 찼을 때부터 답 갱신
            answer = min(answer, stones[dq[0]])
    return answer
