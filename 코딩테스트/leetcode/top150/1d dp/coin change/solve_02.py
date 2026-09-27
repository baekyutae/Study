from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(remaining: int) -> int:
            if remaining == 0:
                return 0

            if remaining < 0:
                return float("inf")

            minimum_count = float("inf")

            for coin in coins:
                minimum_count = min(
                    minimum_count,
                    dfs(remaining - coin) + 1,
                )

            return minimum_count

        answer = dfs(amount)

        if answer == float("inf"):
            return -1

        return answer
