# 커뮤니티 풀이 A — DFS 반환값 합성
# 출처: leetcode.com/problems/number-of-closed-islands/solutions/1250335
#
# 접근:
#   dfs가 "내가 맡은 방향은 닫혀 있나"를 True/False로 돌려준다.
#   물(1)을 만나면 더 갈 데가 없으니 True, 테두리 땅을 밟으면 바깥과 통했으니 False.
#   네 방향 결과를 and로 묶어 한 방향이라도 False면 그 섬 전체가 False가 된다.
#   판정이 재귀 반환값으로 올라오므로 순회를 한 번만 돌면 된다.
#
# 왜 범위 검사가 없나:
#   테두리 칸에서 이미 return False로 끊기므로 재귀가 격자 밖으로 나갈 수 없다.
#   바깥으로 나가는 걸 막는 대신 나가기 직전 줄에서 결론을 낸다.
#   바깥 이중 for문도 range(1, m-1)로 테두리를 건너뛴다.
#
# 왜 visited가 없나:
#   방문한 땅을 물(1)로 덮어쓴다. 찾는 값 0과 덮는 값 1이 절대 안 겹치므로
#   진입부의 grid[i][j] == 1 검사가 방문 검사를 겸한다.
#
# 주의:
#   return dfs(...) and dfs(...) 처럼 한 줄로 쓰면 안 된다.
#   and는 앞이 False면 뒤를 실행하지 않아(단축 평가) 섬의 일부가 방문 표시 없이 남는다.
#   네 결과를 변수에 먼저 받아야 한다.
#
# 시간 O(m*n) / 공간 O(m*n) (재귀 깊이)

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] == 1:
                return True
            if i <= 0 or i >= m - 1 or j <= 0 or j >= n - 1:
                return False

            grid[i][j] = 1

            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            return up and down and left and right

        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0 and dfs(i, j):
                    count += 1

        return count
