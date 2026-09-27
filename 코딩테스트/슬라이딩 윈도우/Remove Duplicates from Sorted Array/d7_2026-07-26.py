class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change_idx = 1

        for serach_idx in range(1, len(nums)):
            if nums[serach_idx] > nums[serach_idx - 1]:
                nums[change_idx] = nums[serach_idx]
                change_idx += 1

        return change_idx
