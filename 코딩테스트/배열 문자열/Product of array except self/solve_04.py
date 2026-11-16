from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        # 각 nums[i]별로 좌측의 누적곱 부터 계산 시작
        left_product = 1  # 좌측 누적곱 시작값 => 좌항이 없으므로 1
        for i in range(len(nums)):
            answer[i] = left_product
            left_product *= nums[i]

        # [1,1,2,6]
        right_product = 1  # 같은 이유로 1
        for j in range(len(nums) - 1, -1, -1):
            # 아까 이미 각 index별 좌측의 누적곱은 구했으니 거기다 우항의 누적곱을 구해 곱한다
            answer[j] = answer[j] * right_product  # 좌측 누적곱에 우측 누적곱을 곱하고
            right_product = nums[j] * right_product  # 다음 연산을 위해 우측 누적곱을 구함

        return answer
