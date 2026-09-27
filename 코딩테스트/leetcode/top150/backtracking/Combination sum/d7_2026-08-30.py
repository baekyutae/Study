class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        # 선택한 candidates의 원소를 target에 빼가며 탐색
        # remaining이 0이되면 조합을 하나 찾았으므로 저장
        # index i 를 인자로 넘겨 가며 탐색해 매 탐색마다 탐색해야할 index의 범위를 명시
        def backtracking(remaining, i):
            if remaining == 0:
                result.append(path.copy())
                return
            if remaining < 0:
                return

            for idx in range(i, len(candidates)):
                number = candidates[idx]
                path.append(number)

                backtracking(remaining-number, idx)
                path.pop()
            return

        backtracking(target,0)
        return result
