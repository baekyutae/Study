from collections import deque
def solution(maps):
    # 출발지에서 레버까지 최단 거리
    # 레버에서 출구 까지 최단거리
    # 둘중 하나라도 벽에 막혀 가지 못한다면 -1 반환
    # else: 두 최단거리의 합을 반환
    
    row, col = len(maps), len(maps[0])
    
    def find(ch):
        for r in range(row):
            for c in range(col):
                if maps[r][c] == ch:
                    return (r,c)
                
    def bfs(start,goal):
        r,c = find(start)
        queue = deque([(r,c,0)])
        visited = {(r,c)}
        
        while queue:
            r,c,dist = queue.popleft()
            print(r,c)
            if maps[r][c] == goal:
                return dist
            
            for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                nr, nc = r+dr, c+dc
                
                if 0<=nr<row and 0<=nc<col and maps[nr][nc] != "X" and (nr,nc) not in visited:
                    queue.append((nr,nc,dist+1))
                    visited.add((nr,nc))
            
        return -1 
    
    find_Lever = bfs("S","L")
    if find_Lever == -1:
        return -1
        
    find_Exit = bfs("L","E")
    if find_Exit == -1:
        return -1
        
    return find_Lever+find_Exit
