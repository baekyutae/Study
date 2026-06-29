import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        주어진 배열에서 k번째로 큰 element를 반환 
        정렬 없이 풀수 있는지?, 강제는 아님

        nums의 원소를 heapq에 저장
        while len(nums) != k 
        길이가 k 가 될때까지 pop
        그리고 heap[0]을 하면 k번째 큰 숫자가 남음

        '''
        heap = []

        for i in nums:
            heapq.heappush(heap, i)

        while len(heap) != k:
            heapq.heappop(heap)

        result = heapq[0]

        return result