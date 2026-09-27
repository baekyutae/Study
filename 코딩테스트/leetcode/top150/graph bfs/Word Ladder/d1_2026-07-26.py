from collections import deque
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # wordlist에서 존재 여부 확인을 빠르게 하기 위해 만듬
        word_set = set(wordList)

        # endword가 wordlist에 없으면 바로 0 반환
        if endWord not in word_set:
            return 0

        visited = set()
        queue = deque()

        queue.append((beginWord, 1))
        visited.add(beginWord)

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    cur_word = word[:i] + c + word[i + 1:]

                    if cur_word not in visited and cur_word in word_set:
                        queue.append((cur_word, length + 1))
                        visited.add(cur_word)

        return 0
