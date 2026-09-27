def solution(triangle):
    dp = [[0] * len(row) for row in triangle]  # triangle에 존재하는 각 좌표에 도달하는 경로의 숫자 합중 가장 큰 값ㅇ르 저장
    dp[0][0] = triangle[0][0]  # 꼭대기는 답이 하나

    # 점화식:
    # 가장자리인 경우: 바로위의 좌표 까지의 누적합에 현재 좌표의 값을 더함
    # 가장자리가 아닌 경우(도달할 수 있는 경로가 좌우 두가지인 경우): 두 경로의 누적합중 더 큰값을 선택해 + 현재 좌표의 값
    for row in range(1, len(triangle)):
        dp[row][0] = dp[row - 1][0] + triangle[row][0]
        dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]

        for col in range(1, row):
            dp[row][col] = triangle[row][col] + max(
                dp[row - 1][col - 1],
                dp[row - 1][col],
            )

    return max(dp[-1])
