# 딕셔너리에 문자가 마지막으로 나온 위치를 저장
# 중복되는 문자를 만나면 마지막으로 나온 위치 + 1 지점으로 left를 이동

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        ans = 0

        for right, char in enumerate(s):
            if char in last_index and last_index[char] >= left:
                left = last_index[char] + 1

            last_index[char] = right
            ans = max(ans, right - left + 1)

        return ans