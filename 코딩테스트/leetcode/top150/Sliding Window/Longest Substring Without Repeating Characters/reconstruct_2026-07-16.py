class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        check = {}
        max_size = 0
        for right in range(len(s)):
            cur_word = s[right]
            if cur_word not in check:
                check[cur_word] = 1
            else:
                check[cur_word] += 1
            if check[cur_word] >= 2:
                while check[cur_word] != 1 and left <= right:
                    if s[left] == cur_word:
                        check[cur_word] -= 1
                        if check[cur_word] == 1:
                            left += 1
                            break
                    check[s[left]] -= 1
                    left += 1

            cur_len = right + 1 - left
            max_size = max(max_size, cur_len)
        return max_size
