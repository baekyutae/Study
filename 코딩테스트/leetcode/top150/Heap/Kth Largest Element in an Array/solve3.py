import heapq
from typing import List
'''
상위 k개만 유지하는 방식
시간 복잡도 : O(N log k)
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
    
