'''
1. 일단 left에 넣는다
2. left 최대값이 right 최소값보다 크면 right로 보낸다
3. 길이 균형을 맞춘다
'''

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # 작은 절반, max heap처럼 사용하기 위해 음수 저장
        self.large = []  # 큰 절반, min heap

    def addNum(self, num: int) -> None:
        # 1. 일단 small에 넣는다.
        heapq.heappush(self.small, -num)

        # 2. small의 최댓값이 large의 최솟값보다 크면 순서가 깨진 것
        # small의 top을 large로 옮긴다.
        if self.large and -self.small[0] > self.large[0]:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # 3. small이 너무 크면 large로 하나 옮긴다.
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # 4. large가 더 커지면 small로 하나 옮긴다.
        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        # small이 하나 더 많으면 small의 top이 중앙값
        if len(self.small) > len(self.large):
            return -self.small[0]

        # 개수가 짝수면 양쪽 top의 평균
        return (-self.small[0] + self.large[0]) / 2