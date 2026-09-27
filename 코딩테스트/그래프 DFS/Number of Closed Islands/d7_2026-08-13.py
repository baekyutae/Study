class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 닫힌섬 갯수 카운트용
        count = 0

        # 격자 크기
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            # grid 범위 밖은 걸러야함
            if not (0<= r <row and 0<= c <col):
                return

            # 육지가 아니라면 걸러야함
            if grid[r][c] != 0:
                return

            # 방문한 영역 표시
            grid[r][c] = 2
            # dfs 탐색
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return

        # 열린 섬 먼저 탐색
        # 행 테두리 탐색
        for r in [0,len(grid)-1]:
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(r,c)

        # 열 테두리 탐색
        for r in range(len(grid)):
            for c in [0,len(grid[0])-1]:
                if grid[r][c] == 0:
                    dfs(r,c)

        # 열린 섬을 다 지웠으니 안쪽에 남은 0이 닫힌섬이다
        for r in range(1,len(grid)-1):
            for c in range(1,len(grid[0])-1):
                if grid[r][c] == 0:
                    dfs(r,c)
                    count +=1

        return count
