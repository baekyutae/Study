from collections import deque

'''
O(n*m)

n*m개의 노드에 대해 처음 방문하는지 확인 : if graph[nx][ny] == 1
=> n*m


n*m개의 노드에서 4방향으로 탐색 가능 확인 : for i in range(4)
=> 4*n*m
-------------------------------
최단 거리 탐색을 위해 bfs 사용
이동 방향을 정의(상하좌우)

인접 노드 탐색을 위한 큐 생성

탐색이 끝날 때 까지 반복
    현재위치에서 갈수 있는 방향을 체크 (상하좌우)
    괴물잉 있거나 미로를 벗어나는 경우 제외
        
    
        좌표에 숫자가 1이면 처음 방문 방문  = 최단 경로
        현재 위치까지의 거리에서 + 1한 값을 탐색 좌표의 값으로 변경 => 시작점 부터 해당 좌표까지의 거리
        처음 탐색한 좌표를 큐에 추가(인접 노드를 계속해서 탐색해 나가기 위해)
        4방향 모두를 확인했다면 for문 종료후 큐에 들어온 순서대로 다시 탐색 시작

큐가 텅빈 상태 즉 탐색이 완료되면(더이상 탐색할 곳이 없으면)
(n,m) 좌표의 값 반환( 시작점 부터의 최단경로)

'''

def maze(x, y,n,m,graph):
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]



