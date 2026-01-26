'''
a,b로 도시간 연결된 도로의 정보를 입력 받되 graph [[],[],[]]
형태로 만들어 graph[index]에서 index가 곧 도시의 번호에 해당되게 만듬
index 리스트안에 연결된 다른 도시 번호들 저장 

최단 거리 초기화

deque에 인접해 방문할 도시 저장
모든 도시 최단거리 탐색 시작
    인접 도시를 하나씩 확인
        방문 하지 않았으면
        최단거리 갱신 : k에서 직전도시까지의 거리 + 1
        방문할 도시 갱신

오름차순으로 최단거리 k인 도시만 출력
최단거리 k인 도시가 없으면 - 1 출력
'''



from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면

        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)