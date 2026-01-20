
'''
O(N*M)

각 격자를 한번씩만 방문하여 0을 1로 바꿈 격자칸수 N*M
---

필요한것:
0으로 이어진 영역(상하좌우 연결) “덩어리” 개수

과정:
모든 칸을 훑는다.
아직 처리 안 된 0을 만나면 => 새 덩어리 발견
덩어리 개수 +1
그리고 그 덩어리 전체를 처리 완료 상태로 만들어서 다시 안 세게 한다.
(i, j)에서 시작해서 연결된 0들을 전부 방문 처리(0→1) 해주는 함수가 필요함



'''

def dfs(x, y, n, m, graph):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y, n, m, graph)
        dfs(x + 1, y, n, m, graph)
        dfs(x, y - 1, n, m, graph)
        dfs(x, y + 1, n, m, graph)
        return True
    return False

def beverage_maker(n, m, graph):
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m, graph):
                result += 1
    return result
