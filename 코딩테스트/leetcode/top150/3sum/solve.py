class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # 조기 종료: 정렬된 상태에서 nums[i]가 양수면 뒤도 모두 양수 -> 합 0 불가능
            if nums[i] > 0:
                break

            # i 중복 스킵: 직전과 같은 값을 고정점으로 다시 쓰면 같은 조합이 또 나옴
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # left 중복 스킵
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right 중복 스킵
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return result