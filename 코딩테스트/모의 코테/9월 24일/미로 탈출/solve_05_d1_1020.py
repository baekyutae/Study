'''
최단시간이 곧 최단거리와 직결되는 문제 -> bfs
2차원 배열 격자 미로: 시작지점, 벽, 통로, 출구, 레버가 존재
시작지점과 레버는 항상 다른위치 존재
모든 지점은 여러번 지나갈수 있음
탈출이 불가하면 -1 반환

시간복잡도
1. xyFinder(point): nm 를 두번 사용 2nm

2. bfs(s,e): 모든지점을 한번씩 방문 + 매번 상하좌우 for문 -> 4nm

o(nm)

공간복잡도
1. visited -> nm

o(nm)
'''
from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    def xyFinder(point):
        # 찾으려는 좌표에 해당하는 문자를 넣으면 좌표를 반환
        for r in range(row):
            for c in range(col):
                if maps[r][c] == point:
                    return (r,c)

    def bfs(s,e):
        visited = set()
        # 문자형태로 시작지점s와 도착지점 e를 넣으면 최댄거리를 반환
        # 시작지점의 좌표를 파악
        # 해당 지점부터 bfs 탐색 시작
        # 만약 현재 탐색 좌표에 문자가 e라면 누적된 거리를 반환하고종료
        # 아니라면
        # maps 범위 내, "x"가 아님, 처음 탐색함 조건을 만족하는 상하좌우 거리1의 좌표를 큐에 추가
        x,y = xyFinder(s)
        queue = deque([(x,y,0)])
        visited.add((x,y))

        while queue:
            r,c,dist = queue.popleft()
            if maps[r][c] == e:
                return dist


            for rMove, cMove in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+rMove, c+cMove
                if 0<=nr<row and 0<=nc<col and maps[nr][nc] != "X" and (nr,nc) not in visited:
                    queue.append((nr,nc,dist+1))
                    visited.add((nr,nc))

        return -1 
                

    toLever = bfs("S","L")
    if toLever == -1: # 도달 불가능한 경우
        return -1
    toExit = bfs("L","E")
    if toExit == -1:
        return -1 

    return toLever+toExit
