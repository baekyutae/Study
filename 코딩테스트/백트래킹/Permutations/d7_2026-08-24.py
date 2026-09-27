class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 탐색 경로를 저장할 자료형
        path = []

        # 탐색 여부 체크를 위한 자료형
        used = [False]*len(nums)

        # 순열 탐색 함수
        def backtracking():

            if len(path) == len(nums):
                result.append(path.copy())


            for i in range(len(nums)):
                number = nums[i]
                if used[i] == True:
                    continue

                path.append(number)
                used[i] = True

                backtracking()

                path.pop()
                used[i] = False

            return

        backtracking()
        return result
