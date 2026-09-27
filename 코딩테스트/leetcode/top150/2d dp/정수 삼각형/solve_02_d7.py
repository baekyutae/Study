def solution(triangle):
    # 최대값을 구하기 위해 기본값은 0으로 설정
    dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    # 사이드 부터 점화식으로 연산
    for row in range(1,len(triangle)):
        dp[row][0] = triangle[row][0] + dp[row-1][0]
        dp[row][row] = triangle[row][row] + dp[row-1][row-1]
        # 그외 영역
        for col in range(1,row):
            dp[row][col] = triangle[row][col] + max(dp[row-1][col-1], dp[row-1][col])

    return max(dp[len(triangle)-1])
