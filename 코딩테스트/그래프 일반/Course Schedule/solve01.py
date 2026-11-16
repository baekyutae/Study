# dfs 방식으로 풀이

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        # 0 = 아직 방문 안 함
        # 1 = 현재 DFS 경로에서 방문 중
        # 2 = 검증 완료

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True