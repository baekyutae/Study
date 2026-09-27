class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #결과 담을
        result = []
        # 순열 경우 탐색해서 임시로 담을
        path = []
        # 사용한 숫자를 또 두번 사용하지 않게 하기 위해
        used = [False]*len(nums)

        # 순열 탐색 함수
        def backtracking():
            # path가 nums와 길이가 같음 -> 순열 하나 완성했으니 저장하고 되돌리기
            if len(path) == len(nums):
                result.append(path.copy())
                return

            # 순열에 숫자 추가를 위한 for문
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtracking()

                # 순열 추가 완료했으면 되돌리기
                used[i] = False
                path.pop()
            return

        backtracking()
        return result
