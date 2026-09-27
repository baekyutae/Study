from typing import List


# 2026-07-15 재구성(reconstruct) 시도 — H1 힌트(유형: 투 포인터)까지 사용
# 읽기 포인터 i, 쓰기 포인터 change_point
# 정렬 배열이므로 nums[i] > nums[i-1] 이면 새로운 고유값
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        change_point = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[change_point] = nums[i]
                change_point += 1

        return change_point
