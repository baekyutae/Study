# sovle 1 과 같은 방식인데 자료형이 set 대신 문자열

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        max_len = 0

        for i in range(len(s)):
            if s[i] in sub:
                max_len = max(max_len, len(sub))

                while s[i] in sub:
                    sub = sub[1:]   # 맨 왼쪽 문자 제거

            sub += s[i]
            max_len = max(max_len, len(sub))

        return max_len