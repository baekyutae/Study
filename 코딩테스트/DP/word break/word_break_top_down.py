from functools import cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = tuple(wordDict)

        @cache
        def can_break(start: int) -> bool:
            if start == len(s):
                return True

            for word in words:
                if s.startswith(word, start) and can_break(start + len(word)):
                    return True

            return False

        return can_break(0)
