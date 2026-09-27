class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 왼쪽에서 오른쪽으로: 왼쪽 누적곱을 answer[i]에 먼저 채워둔다
        left_product = 1
        for i in range(n):
            answer[i] = left_product  # answer[i]를 제외한 좌항의 누적곱을 구함, 처음은 1로 둠. 우항의 누적곱을 곱했을 때 그대로 나와야 하기 때문
            left_product = left_product * nums[i]  # 다음 인덱스를 위해 좌항의 누적곱을 미리 갱신

        # 오른쪽에서 왼쪽으로: 오른쪽 누적곱을 곱해 마무리한다
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right_product
            right_product = right_product * nums[i]

        return answer
