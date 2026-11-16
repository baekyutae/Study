from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount를 만드는 최소 조합을 구하기 위해 1부터 ~ amount 까지 각 금액이 만들어지는 최소 금액을 활용
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    # 점화식: 현재 금액의 최소조합 = min(현재 까지 찾은 가장 작은 조합,  coins에서 고른 새 coin을 뺀 값의 최소 조합+1),
                    # +1은 coin을 더했으니 동전 갯수 +1
                    dp[current_amount] = min(
                        dp[current_amount], dp[current_amount - coin] + 1
                    )

        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
