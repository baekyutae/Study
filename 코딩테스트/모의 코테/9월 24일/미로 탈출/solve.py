'''
풀이: 두 구간(시작 → 레버, 레버 → 출구)을 BFS 함수 하나로 각각 탐색
- 거리는 전체 카운터가 아니라 칸마다 붙는 값이다 → 큐에 (행, 열, 거리)로 넣는다
- 방문 표시는 큐에 넣을 때 하고, 넣는 대상은 이웃 칸이다
- visited는 bfs 안에서 만들므로 호출마다 새로 초기화된다
  (레버 → 출구 구간은 앞 구간에서 지나간 칸을 다시 지나가도 된다)
- 시간 복잡도: O(행 × 열) × 2
'''
from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])

    def find(ch):
        for r in range(rows):
            for c in range(cols):
                if maps[r][c] == ch:
                    return (r, c)

    def bfs(start, goal):
        queue = deque([(start[0], start[1], 0)])   # (행, 열, 거리)
        visited = {start}
        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == goal:
                return dist
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != "X" and (nr, nc) not in visited:
                    visited.add((nr, nc))              # 큐에 넣을 때 방문 표시
                    queue.append((nr, nc, dist + 1))   # 넣는 대상은 이웃 칸
        return -1

    to_lever = bfs(find("S"), find("L"))
    if to_lever == -1:
        return -1
    to_exit = bfs(find("L"), find("E"))
    return -1 if to_exit == -1 else to_lever + to_exit
