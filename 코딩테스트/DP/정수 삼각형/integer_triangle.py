def solution(triangle):
    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]

    for row in range(1, len(triangle)):
        dp[row][0] = triangle[row][0] + dp[row - 1][0]
        dp[row][row] = triangle[row][row] + dp[row - 1][row - 1]

        for col in range(1, row):
            dp[row][col] = triangle[row][col] + max(
                dp[row - 1][col - 1], dp[row - 1][col]
            )

    return max(dp[-1])
