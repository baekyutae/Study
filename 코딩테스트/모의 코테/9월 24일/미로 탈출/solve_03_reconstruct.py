'''
2차원 격자 형태 미로 maps가 주어짐
한칸 이동하는데 1초
각 칸은 벽 아니면  통로

출발점에서 레버를 열고, 탈출구로 가야함

시작지점, 출구, 레버는 항상 다른 좌표에 존재
출구는 레버가 당겨지지 않아도 지나갈수 있으며,모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있다.

-----

2차원 배열에서 최소 == 최단 거리 즉 bfs로 접근 가능
이때 먼저 레버까지의 최단거리
그다음 레버에서 출구 까지의 최단거리
각탐색마다 visited를 초기화 -> 여러번 지나갈수 있으니

레버, 출구 둘중 하나라도 -1 즉 도달 못하면 solution은 -1 반환


시간복잡도
1. xyFinder 두번 호출 2n^2
2.findBfs 에 while문은 통로인 모든 좌표를 탐색, 벽이 없는 케이스 고려하면 n^2
거기다가 매 방문마다 for dr,dc
4n^2

o(n^2)

공간복잡도
o(1)

edgecase
1. 레버 or 출구가 x로 막힌 케이스: -1 반환
'''
from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])

    def xyFinder(ch):# 원하는 지점의 좌표 반환
        for r in range(row):
            for c in range(col):
                if maps[r][c] == ch:
                    return [r,c]


    def findBfs(start, end): # 최단거리 반환
        # 탐색 시작지점 좌표 부터 탐색
        r,c = xyFinder(start)
        queue = deque([(r,c,0)]) # 탐색 시작 지점과 탐색 거리
        visited = set([(r,c)])

        while queue:
            r,c,dist = queue.popleft()
            if maps[r][c] == end:
                return dist
            for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):# 상하좌우 탐색
                nr, nc = r+dr, c+dc
                # nr nc 가 maps 범위 내, 벽 아님, 방문 했던 좌표 아닐시 queue에 추가
                if 0<=nr<row and 0<=nc<col and maps[nr][nc] != "X" and (nr,nc) not in visited:
                    queue.append((nr,nc,dist+1))
                    visited.add((nr,nc))

        return -1 # 도달 불가시 -1


    toLever = findBfs("S","L")
    if toLever == -1:
        return -1
    toExit = findBfs("L","E")
    if toExit == -1:
        return -1

    return toLever+toExit
