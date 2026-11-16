class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        check = {}
        max_len = 0
        for right in range(len(s)):
            word = s[right]

            # check 안에 추가
            if word not in check:
                check[word] = 1
            else:
                check[word] += 1

            # 중복이 발생한다면?
            if check[word] >= 2:
                while check[word] != 1 and left<=right:
                    # 현재 단어가
                    cur_word = s[left]
                    # 중복인 단어라면
                    if cur_word == word:
                        check[cur_word] -= 1 # 중복에서 제거
                        left += 1 # 이동
                        if check[cur_word] == 1: # 만약 중복이 완전히 제거되었으면 종료
                            break

                    else:
                        check[cur_word] -= 1
                        left += 1

            cur_len = right+1-left # 현재길이: 한글자는 right-left가 0이니 식에 +1을 더해줌
            max_len = max(max_len, cur_len)

        return max_len
