class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_k = k%len(nums) 
        left= 0
        right = len(nums)
        # 전체 뒤집기
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -=1

        # 맨앞에서 k개만 뒤집기
        
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right -= 1