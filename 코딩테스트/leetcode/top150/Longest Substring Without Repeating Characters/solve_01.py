# 슬라이딩 윈도우를 이용해
# 중복되는 문자를 만날 때마다 제거해나가며 가장 긴 길이를 ans에 저장

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])
            ans = max(ans, right-left +1)

        return ans