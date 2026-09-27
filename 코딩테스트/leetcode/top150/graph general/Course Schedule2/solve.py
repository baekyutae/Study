from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        result = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            cur_course = queue.popleft()
            result.append(cur_course)

            for next_course in graph[cur_course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return result if len(result) == numCourses else []
