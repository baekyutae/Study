# 커뮤니티 풀이 B — 테두리 씨앗 DFS
# 출처: leetcode.com/problems/number-of-closed-islands/solutions/4216640
#
# 접근:
#   열린 섬은 반드시 테두리 칸 하나를 포함한다("닫힌 섬이면 테두리에 안 닿는다"의 대우).
#   그래서 테두리 칸에서만 dfs를 시작해도 열린 섬을 하나도 빠뜨리지 않는다.
#   1) 네 변의 칸에서 dfs를 돌려 열린 섬을 전부 2로 지운다.
#   2) 남은 0을 훑으면서 dfs로 그 섬을 2로 지우고 1개로 센다.
#
# solve.py(내 풀이)와 다른 점:
#   테두리 칸을 찾으려고 격자 전체를 훑지 않고 좌표로 직접 열거한다.
#   check 함수와 첫 번째 전체 순회가 통째로 사라진다.
#   visited 집합 없이 grid = 2 마킹 하나로 방문 표시를 통일해 튜플 해싱 비용도 없다.
#
# dfs 하나가 두 역할을 겸하는 이유:
#   1단계에서는 "열린 섬 지우개", 2단계에서는 "센 섬 지우개"인데
#   하는 일이 둘 다 "0으로 연결된 덩어리를 2로 바꾸기"로 같아서 함수를 나눌 필요가 없다.
#   지운 칸을 나중에 다시 볼 일이 없으므로 왜 지워졌는지 구분하지 않아도 된다.
#
# 시간 O(m*n) / 공간 O(m*n) (재귀 깊이)
# 원본 해설은 O(m+n)이라고 적었는데 틀렸다. 마지막 이중 for문만 봐도 O(m*n)이다.

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col) or grid[r][c] != 0:
                return

            grid[r][c] = 2

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1단계: 테두리에 닿은 섬(= 열린 섬)을 전부 지운다
        for r in range(row):
            dfs(r, 0)
            dfs(r, col - 1)
        for c in range(col):
            dfs(0, c)
            dfs(row - 1, c)

        # 2단계: 남은 0은 전부 닫힌 섬이므로 세기만 하면 된다
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    dfs(r, c)
                    count += 1

        return count
