class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(start, remaining):
            if remaining == 0:            # 정확히 도달 → 저장
                result.append(path.copy())
                return
            if remaining < 0:             # 초과 → 가지치기
                return
            for i in range(start, len(candidates)):  # ← 규칙: start 앞은 안 본다
                path.append(candidates[i])
                backtracking(i, remaining - candidates[i])  # ← i를 그대로 넘김: 같은 원소 재사용 허용
                path.pop()

        backtracking(0, target)
        return result
