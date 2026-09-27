import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 탐색 속도 개선
        word_set = set(wordList)

        # endword가 wordlist에 존재하지 않는 경우
        if endWord not in word_set:
            return 0

        # bfs니 탐색한 단어를 체크
        visited = set()
        # 탐색 단어를 넣을 큐
        queue = deque()

        visited.add(beginWord)
        queue.append((beginWord, 1))  # 매탐색 레벨마다 탐색한 거리를 기록, 1부터 시작

        while queue:
            word, length = queue.popleft()

            # endWord에 도달하면 최단 거리 반환
            if word == endWord:
                return length

            # 다음 탐색 단어 존재 여부 확인
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, length + 1))
                        visited.add(next_word)

        # endword가 wordlist에 있지만 중간에 이어줄 단어가 없는경우
        return 0
