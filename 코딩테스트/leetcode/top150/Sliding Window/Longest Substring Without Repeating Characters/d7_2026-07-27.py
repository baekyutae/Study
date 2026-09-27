class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dup_check = {}
        longestword = 0

        # substring 생성 시작
        for right in range(len(s)):
            word = s[right]
            if word not in dup_check:
                dup_check[word] = 1

            else:
                dup_check[word] += 1

                if dup_check[word] >= 2:
                    # 중복 발견시 중복 제거
                    while dup_check[word] > 1:
                        cur_word = s[left]
                        dup_check[cur_word] -= 1
                        left += 1

            cur_len = right + 1 - left
            longestword = max(longestword, cur_len)

        return longestword
