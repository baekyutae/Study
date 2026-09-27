class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        dp[0] = nums[0]
        if len(nums) >= 2:
            dp[1] = max(nums[0],nums[1]) # [5,1] 이면 idx 1인 집은 안털고 0만 터는게 이득임

        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx-1], dp[idx-2]+nums[idx])


        return dp[-1]
