'''
1. 문제 유형 파악 

최단시간 == 최단거리
출발지에서 레버까지의 최단거리와, 레버에서 출구 까지의 최단거리를 구해야함

최단거리 -> bfs



2. 엣지케이스
레버 또는 출구가 "X"로 둘러쌓인 경우: 둘중 하나라도 -1을 반환시 전체 Solution 함수도 -1 반환

3. 시간/공간복잡도



'''
from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])

    # maps상에 문자를 입력하면 좌표를 반환
    def loc(ch):
        for x in range(row):
            for y in range(col):
                if maps[x][y] == ch:
                    return x,y

    # 출발지와 목적지를 알려주면 최단거리를 구해 반환
    def bfs(s,e):
        visited = set()
        queue = deque()
        # 탐색을 시작할 좌표 설정
        x,y = loc(s)
        # 큐에 시작 좌표 추가 및 방문처리
        queue.append((x,y,0))
        visited.add((x,y))

        # 탐색시작
        while queue:
            # 목적지에 도달하면 탐색 종료하고 거리 반환
            r,c,t = queue.popleft()
            if maps[r][c] == e:
                return t

            # 상하좌우 탐색을 이어가는데
            # 벽, maps 범위 밖, 이미 탐색한 영역은 제외
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                next_r,next_c = r+dr, c+dc 
                if 0<=next_r<row and 0<=next_c<col and maps[next_r][next_c] != "X" and (next_r,next_c) not in visited:
                    queue.append((next_r,next_c,t+1))
                    visited.add((next_r,next_c))
        return -1 

    StoL = bfs("S","L") 
    LtoE = bfs("L","E") 

    if StoL == -1 or LtoE == -1:
        return -1

    else:
        return StoL+LtoE    
    
