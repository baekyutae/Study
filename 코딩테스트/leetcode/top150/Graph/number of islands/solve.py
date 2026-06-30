'''
이 문제는 모든 칸을 최대 한 번 방문한다.
각 칸에서 상하좌우 4개만 본다.
따라서 O(row * col)


'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        row_count = len(grid)
        col_count = len(grid[0])

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1

                    queue = deque([(r,c)])
                    visited.add((r,c))

                    while queue:
                        cur_r, cur_c = queue.popleft()

                        for dr, dc in directions:
                            nr = cur_r + dr
                            nc = cur_c + dc

                            if 0 <= nr < row_count and 0<= nc < col_count and grid[nr][nc] == "1" and (nr,nc) not in visited:
                                visited.add((nr,nc))
                                queue.append((nr,nc))
        return count

