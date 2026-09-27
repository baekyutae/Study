from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change_index = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[change_index] = nums[i]
                change_index += 1

        return change_index
