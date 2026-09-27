from typing import List


# 2026-07-15 재구성(reconstruct) 시도 — 힌트 0회(H0)
# 3단 뒤집기: 전체 뒤집기 → 앞 k개 뒤집기 → 나머지 뒤집기
# 첫 제출은 3단계(나머지 뒤집기) 누락으로 실패, 자력 수정 후 통과
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        new_k = k % len(nums)
        left = 0
        right = len(nums) - 1
        # 전체 뒤집기
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 맨앞에서 k개만 뒤집기
        left = 0
        right = new_k - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # 나머지 구간 뒤집기
        left = new_k
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
