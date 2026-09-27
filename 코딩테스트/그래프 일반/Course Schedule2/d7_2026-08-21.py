class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        status = [0]*numCourses

        def search(course):
            if status[course] == 1:
                return False
            
            if status[course] == 2:
                return True

            # 이미 수강완료 or 사이클이 아님을 확인했으니 탐색 진행 처리
            status[course] = 1

            # 현재과목을 선행으로 하는 후행과목들 탐색
            for next_course in graph[course]:
                # 탐색 도중 False를 반환하면 전체 과목 수강 불가 처리
                if not search(next_course):
                    return False
            # False처리 되지 않아야 여기로 옴
            # 코스하나가 끝까지 다 정상 수강가능함을 확인했으니 수강완료 처리 및 result에 담은뒤 반환 
            status[course] = 2
            result.append(course)

            return True

        # 각 과목을 시작점으로 코스 탐색
        # 코스가 무조건 0부터 시작하는게 아니므로 다 탐색해봐야함
        for i in range(numCourses):
            if status[i] == 0:
                if not search(i):# 반환한 False를 여기서 받아서 [] 반환
                    return []


        result.reverse()
        return result
