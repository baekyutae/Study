import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        k번째 큰 원소를 찾아 반환
        nums의 원소를 전부 음수 형태로 heap에 저장
        k번째 꺼낸 숫자를 다시 양수로 변환하면 k번째로 큰수

        시간복잡도 : O(N log N + k log N)

        '''

        heap = []
        count = 0
        for i in nums:
            heapq.heappush(heap, -i)

        while count < k-1:
            heapq.heappop(heap)
            count += 1

        result = -heapq.heappop(heap)
        return result
        
