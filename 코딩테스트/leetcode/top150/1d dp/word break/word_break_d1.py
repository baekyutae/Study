from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s) + 1):
            for start in range(end):
                dp[end] = dp[start] and s[start:end] in wordSet
                if dp[end]:
                    break

        return dp[len(s)]
