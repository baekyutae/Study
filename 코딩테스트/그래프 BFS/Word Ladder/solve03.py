# 후보 생성 + set 조회 방식 => o(m * l * 26) 최대 약 130만회 연산
# solve02.py의 wordList 전체 순회(약 2억5천만회)를 이 방식으로 대체
# m: wordlist 길이 (큐에 적재되는 단어 수 상한)
# l: 단어 길이, 한 자리씩 a~z 26자를 대입해 word_set에 있는지 조회
#
# invariant
# 1. 큐에 넣을 때 visited에 추가한다 => 같은 단어가 두 번 들어가지 않는다
# 2. popleft로 꺼내므로 큐 안의 length는 비내림차순이다 => 처음 만난 endWord가 최단

from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # 방문여부 체크용
        visited = set()

        # 탐색용 큐
        queue = deque()
        queue.append((beginWord, 1))  # 시작단어도 경로 거리에 포함

        # 한글자 바뀐 단어가 wordlist에 있는지 찾기 빠르게 하기위해
        word_set = set(wordList)

        # endword가 word list에 없으면 바로 종료
        if endWord not in word_set:
            return 0

        # 탐색 시작
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            # 현재 word에서 한글자 차이나는 단어를 word_set에 대입해가며 탐색
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    change_word = word[:i] + c + word[i + 1:]
                    if change_word in word_set and change_word not in visited:
                        queue.append((change_word, length + 1))
                        visited.add(change_word)

        # 경로가 없으면
        return 0
