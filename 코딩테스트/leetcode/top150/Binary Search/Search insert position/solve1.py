class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        배열이 이미 정렬됨

        가운데 인덱스 = mid
        left <= right 인동안 반복 하며 탐색

        nums[mid] == target이면
            return mid
        nums[mid] 가 target 보다 크면 left = mid+1
        작으면 right = mid -1 

        배열에 없으면?
 
        edge case
        1. 길이가 1인 배열
        2. target이 배열에 존재하지 않는 경우
        '''
        left = 0
        right = len(nums) -1 


        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            elif nums[mid]<target:
                left= mid+1

            else:
                right = mid - 1

        if mid == 0:
            if nums[mid] > target:
                return mid
            else:
                return mid+1

        else:
            if nums[mid] > target:
                return mid
            else:
                return mid+1