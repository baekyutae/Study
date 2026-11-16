'''
풀이 4: 레버에서 BFS 한 번으로 두 거리를 동시에 구함, 시간·공간 O(R×C)
- 이동이 양방향이고 한 칸 비용이 모두 1이라 S→L 거리 = L→S 거리
- 레버에서 퍼지며 모든 칸의 최단 거리를 dist에 기록하면 dist[S], dist[E]가 필요한 두 거리
- dist 하나가 방문 여부(-1 = 미방문)와 거리를 함께 담음
- 해설: 레버 BFS 풀이 해설.md
'''

from collections import deque


def solution(maps):
    R, C = len(maps), len(maps[0])
    pos = {maps[r][c]: (r, c) for r in range(R) for c in range(C) if maps[r][c] in "SLE"}

    dist = [[-1] * C for _ in range(R)]   # -1 = 아직 못 감(방문 기록 겸용)
    lr, lc = pos["L"]
    dist[lr][lc] = 0                      # 출발점: 거리 기준점 + 방문 표시
    q = deque([(lr, lc)])
    while q:
        r, c = q.popleft()
        for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != "X" and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    toS = dist[pos["S"][0]][pos["S"][1]]  # 레버↔시작점
    toE = dist[pos["E"][0]][pos["E"][1]]  # 레버↔출구
    return -1 if toS == -1 or toE == -1 else toS + toE
