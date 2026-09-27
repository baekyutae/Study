# 단어끼리 한글짜식 비교하는 방식 => 비추 o(m^2 * l) 최대 약 2억5천만회 연산
# m: wordlist 길이 (for word in wordList)
# m: 큐에 적재된 문자 개수, 최악의 경우 begin word 부터 endword까지 하나씩 달라지며 이어진다면 m+1 => 대략 m과 같다 볼수도 잇음
# l: 단어길이만큼 비교 ( for i in range(len(cur_word)))

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        visited = set()
        diff_count = 0
        length = 1
        
        queue.append((beginWord,length))
        visited.add(beginWord)
     
        while queue:
            diff_count = 0
            cur_word,cur_len = queue.popleft()

            if cur_word == endWord:
                return cur_len

            for word in wordList:
                if word in visited:
                    continue
                for i in range(len(cur_word)):
                    if word[i] != cur_word[i]:
                        diff_count += 1
                if diff_count == 1:
                    queue.append((word,cur_len+1))
                    visited.add(word)
                diff_count = 0
               
        return 0    