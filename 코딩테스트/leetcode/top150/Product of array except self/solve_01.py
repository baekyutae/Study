class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 1) 왼쪽 누적곱 저장
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i] # 다음 칸을 위한 왼쪽 누적곱으로 업데이트

        # 2) 오른쪽 누적곱을 곱해 최종 완성
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer



'''
left_product는 왼쪽에서 오른쪽으로 가며 왼쪽 누적곱을 들고 다니는 변수
right_product는 오른쪽에서 왼쪽으로 가며 오른쪽 누적곱을 들고 다니는 변수
'''