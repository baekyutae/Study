# 전치 → 각 행 뒤집기

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. 주 대각선 전치
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. 각 행 뒤집기
        for row in matrix:
            row.reverse()