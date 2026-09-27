from collections import deque
import string 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # 일단 bfs를 할려면 중복 방문은 안되닌 체크용
        visited = set()

        # 탐색을 위해
        queue = deque()
        # deadend로 경로가 빠지지 않게 하기 위한 체크 비용 o(1)로
        dead_set = set(deadends)
        if target in dead_set:
            return -1 

        # "0000" 에서 시작
        if "0000" not in dead_set:
            visited.add("0000")
            queue.append(("0000",0))


        # 탐색 루프
        while queue:
            number, length = queue.popleft()

            if number == target:
                return length

            # 현재의 문자형태 숫자를 한자리씩 바꿔가며 0~9를 대입
            # deadend에 없다? 그럼 큐에 추가
            # 있으면? 건너뛰어
            for i in range(len(number)): # 돌릴 다이얼을 선택 (0~3)
                for n in [(int(number[i])+1) % 10, (int(number[i])+9) % 10]:
                    str_n = str(n)
                    new_number = number[:i] + str_n + number[i+1:]
                    if new_number not in dead_set and new_number not in visited:
                        queue.append((new_number,length+1))
                        visited.add(new_number)

        return -1
