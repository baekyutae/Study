from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. 상하 반전
        # 첫 번째 행 ↔ 마지막 행
        # 두 번째 행 ↔ 뒤에서 두 번째 행
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

        # 2. 주 대각선 전치
        # matrix[i][j] ↔ matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]