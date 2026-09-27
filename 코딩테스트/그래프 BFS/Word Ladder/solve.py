'''
N = wordList의 단어 개수
L = 단어 길이

모든 단어를 한번씩 방문 N
단어 길이 * 각 단어별 a-z 로변환 26*L

전체: N*L*26

상수제외하면 시간복잡도는 O(N*L)

'''

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList) # next_word in word_set 여기서 검색속도를 위해 set자료형 사용

        if endWord not in word_set:
            return 0

        q = deque()
        q.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i + 1:]

                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, length + 1))

        return 0