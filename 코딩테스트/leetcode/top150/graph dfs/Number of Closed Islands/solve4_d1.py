class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # dfs 탐색
        def dfs(r,c):
            # r,c 가 범위 밖의 좌표거나 좌표값이 0이 아니라면
            # return
            if not (0<=r<row and 0<=c<col):
                return

            if grid[r][c] !=0:
                return 
             

            # 현재 탐색 좌표가 테두리에 맞닿아 있으면
            # 현재좌표값을 2로 변환
            # 또한 닫힌섬 탐색에서 이미 탐색한 영역으 2로 체크 하는 역할
            grid[r][c] = 2
                
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return 
            # 상하좌우로 dfs 함수 탐색
            # return : 반환값은 따로 필요없음


        # 열린 섬은 무조건 테두리에 닿아 있음
        # 테두리에서 시작하는 dfs 탐색으로 열린섬에 해당하는 육지 좌표값으 2로 변환

        #  테두리행 dfs 탐색
        for r in range(row):
            for c in [0,col-1]:
                if grid[r][c] == 0:
                    dfs(r,c)
            
        # 테두리 열 dfs 탐색
        for c in range(col):
            for r in [0,row-1]:
                if grid[r][c] == 0:
                    dfs(r,c)

        # 이제 열린함수 영역 2로 처리 완료 
        # 테두리 안쪽 좌표범위에서 좌표순회
        # r,c가 0이라면 dfs 탐색 및 닫힌 섬의 개수+1
        count = 0
        for r in range(1,row-1):
            for c in range(1,col-1):
                if grid[r][c] == 0:
                    dfs(r,c)
                    count +=1

        return count
