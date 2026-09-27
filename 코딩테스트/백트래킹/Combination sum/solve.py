from typing import List


class Solution:
    def combinationSum(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:
        result = []
        path = []

        def dfs(start: int, remaining: int) -> None:
            # 정확히 target을 만든 경우
            if remaining == 0:
                result.append(path[:])
                return

            # target을 초과한 경우
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                number = candidates[i]

                # 선택
                path.append(number)

                # 같은 숫자를 다시 사용할 수 있으므로 i부터 탐색
                dfs(i, remaining - number)

                # 선택 취소
                path.pop()

        dfs(0, target)
        return result