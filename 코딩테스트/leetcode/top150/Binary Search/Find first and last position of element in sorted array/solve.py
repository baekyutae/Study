from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def find_first():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid          # 일단 후보 저장
                    right = mid - 1       # 더 왼쪽에도 target 있는지 확인

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        def find_last():
            left = 0
            right = len(nums) - 1
            answer = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    answer = mid          # 일단 후보 저장
                    left = mid + 1        # 더 오른쪽에도 target 있는지 확인

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return answer

        first = find_first()
        last = find_last()

        return [first, last]