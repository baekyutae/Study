class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(idx, remain):
            if remain == 0:
                result.append(path.copy())
                return 

            if remain < 0:
                return

            for i in range(idx,len(candidates)):
                number = candidates[i]
                path.append(number)

                backtracking(i,remain-number)

                path.pop()

            return 

        backtracking(0,target)
        return result
