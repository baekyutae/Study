from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque([(r, c)])
            board[r][c] = "S"  # Safe

            while queue:
                cur_r, cur_c = queue.popleft()

                for dr, dc in directions:
                    nr = cur_r + dr
                    nc = cur_c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        board[nr][nc] == "O"
                    ):
                        board[nr][nc] = "S"
                        queue.append((nr, nc))

        # 1. 위/아래 border 확인
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)

            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)

        # 2. 왼쪽/오른쪽 border 확인
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)

            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)

        # 3. 남은 O는 캡처, S는 복구
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"