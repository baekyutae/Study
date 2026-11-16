class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1) # 0번째 계단 즉 가만히 있는 경우도 포함해야 불변식이 세워짐
        memo[1] = 1
        memo[0] = 1

        for i in range(2,n+1):
            memo[i] = memo[i-1]+memo[i-2]


        return memo[n]
