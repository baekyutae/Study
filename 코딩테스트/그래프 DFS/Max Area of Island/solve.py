from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()

        # 육지 탐색 함수
        def search(r, c):
            # grid 범위 밖이면 0 반환
            if not (0 <= r < row and 0 <= c < col):
                return 0

            # 바다이거나 이미 방문한 육지면 0 반환
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            # 방문 처리
            visited.add((r, c))

            # 섬 넓이 반환, 1은 (r, c) 자기 자신
            return 1 + search(r + 1, c) + search(r - 1, c) + search(r, c + 1) + search(r, c - 1)

        # grid에서 육지를 찾아 탐색을 시작함
        max_size = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    cur_size = search(i, j)
                    max_size = max(max_size, cur_size)

        return max_size
