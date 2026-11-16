class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 방문한곳을 또 방문하지 않기 위해
        visited = set()

        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            # 범위 밖인 경우를 차단
            if not 0<=r<row or not 0<=c<col:
                return 0

            if (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            # 현재 위치가 육지니 넓이 1 그리고 상하좌우로 탐색한 넓이를 더해서 반환
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        # 육지 탐색 및 dfs 트리거
        max_size = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c)not in visited:
                    cur_size = dfs(r,c)

                    max_size = max(max_size, cur_size)

        return max_size
