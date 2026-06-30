# 전체 시간복잡도는 `O(n + e)`

from collections import deque
from typing import List

class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:
        graph = [[] for _ in range(n)]

        # 1. 양방향 그래프 만들기
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 2. source부터 BFS 시작
        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()

            # 3. destination에 도착하면 True
            if node == destination:
                return True

            # 4. 현재 노드에서 갈 수 있는 이웃 탐색
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

        # 5. 끝까지 못 찾으면 False
        return False
    

