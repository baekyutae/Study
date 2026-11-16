class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        경우의 수가 두가지: 
        1. 현재집을 터는경우: 직전집 i-1은 못털고 i-2번째 집까지 털때 가장 큰금액 dp[i-2] + 현재 집에 돈 nums[i]
        2. 현재집을 털지 않는 경우: 직전집 i-1까지 털때 가장 큰금액 dp[i-1]
        '''
        dp = [0]*len(nums)
        dp[0] = nums[0]
        if len(nums)>=2:
            # 경우가 두가지, 1번집을 터느냐 0번집을 터느냐 => 더 큰값 선택
            dp[1] = max(dp[0], nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])


        return max(dp)
