from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        '''
        수강과목간의 선/후행 관계를 그래프로 표현한뒤
        dfs 로 가장 처음 들어야할 과목부터 마지막 후행과목 까지 탐색후
        마지막 과목부터 order에 저장
        order.reverse()로 반환
        '''
        # 각 과목별로 해당과목을 선수과목으로 두는 후행 과목들을 그래프 형태로 정리
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        # 각 과목의 상태를 표시
        # 0: 아직 시작전, 1: 탐색중, 2: 수강 완료
        status = [0] * numCourses

        order = []

        # 과목 관계 그래프를 탐색할 dfs 함수
        def dfs(node):
            # 탐색중인 과목을 다시 만난다는건 선/후행 관계간에 순환 참조가 존재 하므로 False 반환
            if status[node] == 1:
                return False
            if status[node] == 2:
                return True

            # 탐색 시작 했으니 1
            status[node] = 1

            # 연결된 과목들 탐색
            for next_node in graph[node]:
                if not dfs(next_node):  # 사이클이 발생해 False를 반환하면
                    return False

            status[node] = 2  # 현재 과목을 선수로 두는 과목들을 들었으므로 현재 과목도 status =2
            order.append(node)

            return True

        # 각 과목별로  탐색 시작
        for node in range(numCourses):
            if not dfs(node):  # 탐색중에 사이클이 존재하므로 빈배열 반환
                return []

        # reverse()는 제자리에서 뒤집고 None을 반환하므로 반환문과 분리한다
        order.reverse()
        return order
