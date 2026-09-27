from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 방문한 좌표 표기
        visited = set()
        row = len(grid)
        col = len(grid[0])

        # 닫힌 섬 개수
        count = 0

        # 현재 좌표의 상하좌우 좌표가 범위 안인지 체크하는 함수
        def check(r, c):
            result = True
            if not 0 <= r - 1 < row:
                return False
            if not 0 <= r + 1 < row:
                return False
            if not 0 <= c - 1 < col:
                return False
            if not 0 <= c + 1 < col:
                return False

            return result

        # 제외할 dfs 섬 영역 체크
        # 0을 0->2로 변경
        def except_island(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return
            if (r, c) in visited or grid[r][c] != 0:
                return

            visited.add((r, c))
            grid[r][c] = 2

            except_island(r + 1, c)
            except_island(r - 1, c)
            except_island(r, c + 1)
            except_island(r, c - 1)
            return

        # 제외해야할 섬들 탐색
        # 시작점 좌표값이 0이면서, 상하좌우 최소 한군데가 좌표가 grid 범위 밖인 좌표
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 and not check(r, c) and (r, c) not in visited:
                    except_island(r, c)

        # 닫힌 섬 영역 탐색 함수

        def closed_island(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return

            if (r, c) in visited or grid[r][c] != 0:
                return

            visited.add((r, c))

            closed_island(r + 1, c)
            closed_island(r - 1, c)
            closed_island(r, c + 1)
            closed_island(r, c - 1)

            return

        # 닫힌 섬 갯수 카운트
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0 and (r, c) not in visited:
                    closed_island(r, c)
                    count += 1

        return count
