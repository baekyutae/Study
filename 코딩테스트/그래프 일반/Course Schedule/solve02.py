from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        finished = 0

        while q:
            current = q.popleft()
            finished += 1

            for next_course in graph[current]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        return finished == numCourses
    
    '''
    graph: 코스별로 해당 코스를 선수강 해야하는 조건의 코스들을 인접리스트로 저장
    indegree: 각 코스를 듣기 위해 아직 필요한 선수과목의 개수

    for graph 생성:
        graph[선수과목].append(이 선수과목을 필요로 하는 후행 과목들)
        indegree[코스 번호] += 1

    q = deque()  => 선수강 과목을 다들어 수강 가능한 과목을 저장

    for course in range(numCourses):
        if 해당 과목의 남은 선수과목 수가 0이라면:
            q.append(course)

    finished = 0 : 들은 과목수

    while q:
        현재 수강 과목 = q.popleft()
        finished += 1

        for 현재 과목을 선수과목으로 필요로 하는 후행 과목들을 하나씩 확인:
            inegree[다음과목] -= 1 => 현재수강과목이 다음 과목의 선수강 과목

            if 다음과목이 선수강 과목을 다들은 과목이라면:
                q.append(다음과목)

    finished == numCourses이면 모든 과목을 수강 가능한 순서로 처리했다는 뜻이므로 True.
    finished < numCourses이면 사이클 때문에 끝까지 처리하지 못한 과목이 남았으므로 False.
    '''