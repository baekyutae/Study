class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        wordSet = set(wordDict)

        # 확인하려는 범위 end
        for end in range(1,len(s)+1):
            for start in range(end):
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True

        return dp[len(s)]
