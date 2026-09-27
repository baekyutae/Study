# https://leetcode.com/problems/fruit-into-baskets/
# 2026-07-30 transfer 시도 (원본: Longest Substring Without Repeating Characters)
# 결과: Accepted, Runtime 197ms (Beats 29.59%)
# 시간 O(n), 공간 O(1)
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 종류 체크
        check = {}
        left = 0

        max_fruit = 0

        #우측으로 이동하며 과일을 담음
        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit not in check:
                check[fruit] = 1

            else:
                check[fruit] += 1

            # 이미 두 바구니에 두종류의 과일이 담겼다면,
            if len(check) >= 3:
                while len(check) >= 3:
                    cur_fruit = fruits[left]
                    check[cur_fruit] -= 1
                    if check[cur_fruit] == 0:
                        del check[cur_fruit]
                    left += 1

            fruit_count = right + 1 - left
            max_fruit = max(max_fruit, fruit_count)

        return max_fruit
