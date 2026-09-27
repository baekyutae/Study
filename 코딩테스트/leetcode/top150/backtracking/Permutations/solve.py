class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []

        def dfs():
            if len(temp) == len(nums):
                result.append(temp[:])
                return

            for num in nums:
                if num in temp:
                    continue

                temp.append(num)
                dfs()
                temp.pop()

        dfs()
        return result