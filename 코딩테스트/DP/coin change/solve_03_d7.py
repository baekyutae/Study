class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # 최소값을 구하므로 일단 초기값은 무한으로 설정 -> 어떤 dp[i-coin]이던 해당 값을 최소값으로 지정하기 위해
        dp = [float("inf")]*(amount+1)
        dp[0] = 0 # 0을 만드는건 동전 사용 0

        for i in range(1,amount+1):
            for coin in coins:
                if i>=coin: # 구하려는 값 i 보다 coin이 작은 경우만 성립
                    dp[i] = min(dp[i-coin]+1,dp[i]) #점화식: 이전에 구한 dp[i]값과 비교하여 최솟값을 구한다

        if dp[amount] == float("inf"): # 만약 최소값을 구하지 못했다면 -1 반환
            return -1

        else:
            return dp[amount]
