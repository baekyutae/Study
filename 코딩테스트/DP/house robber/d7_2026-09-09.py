from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 위치별 최대 금액 저장
        money = [0] * len(nums)

        # 불변식 성립을 위해 값 정의
        money[0] = nums[0]
        # 만약 nums의 길이가 1인 경우 그냥 money[1] = nums[1] 이라 정의하면 indexerror 발생
        if len(nums) >= 2:
            money[1] = max(nums[0], nums[1])

        # 일단 세운 점화식이
        # max(지금집 털고 +  그 전전집 까지 턴 최대값, 전집까지 턴 최대값  )
        # 두번째 집부터 털때 최대금액을 점화식을 활용해 갱신해 나간다

        for i in range(2, len(nums)):
            money[i] = max(money[i - 2] + nums[i], money[i - 1])

        # 계속 최대값을 갱신해 나가는 구조이므로 마지막 위치에서의 금액이 가장큼
        return money[-1]
