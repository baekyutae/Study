from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        words = tuple(wordDict)
        queue = deque([0])
        visited = {0}

        while queue:
            start = queue.popleft()

            for word in words:
                end = start + len(word)
                if not s.startswith(word, start):
                    continue
                if end == len(s):
                    return True
                if end not in visited:
                    visited.add(end)
                    queue.append(end)

        return False
