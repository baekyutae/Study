class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        check = {}

        for right in range(len(s)):
            word = s[right]
            # substring에 추가
            if word in check:
                check[word] += 1
            else:
                check[word] = 1

            # 중복 발생시
            if check[word] >= 2:
                # 중복 제거할때까지 왼쪽 포인터를 이동해가며 딕셔너리에도 반영
                while check[word] != 1 and left<=right:
                    cur_word = s[left]
                    if cur_word == word:
                        check[cur_word]-= 1
                        left+=1
                        # 중복 제거가 완료되면 종료
                        if check[cur_word] == 1:
                            break
                    # 중복 제거가 완료될 때까지 이동
                    else:
                        check[cur_word] -= 1
                        left+=1
            # 최대 길이 갱싱
            cur_len = right+1-left
            max_length = max(max_length, cur_len)

        return max_length
