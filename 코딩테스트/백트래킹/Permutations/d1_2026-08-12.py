class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 일단 사용여부를 변경할 상태 저장소
        used = [False] * len(nums)

        # 순열을 만들어 저장할 리스트
        path = []

        # 최종 결과를 담을
        result = []

        def backtracking():
            # 우선 탐색 종료 조건부터
            # 순열이 하나 완성되면 결과를 저장하고 종료 -> 되돌리기로
            if len(path) == len(nums):

                result.append(path.copy())
                return

            # 순열 path에서 다음 자리에 올 숫자 nums에서 고르기
            for i in range(len(nums)):
                # 이미 사용한 숫자는 안됨
                if used[i] == True:
                    continue
                # path에 추가
                path.append(nums[i])
                used[i] = True

                #다음 탐색
                backtracking()

                # 탐색이끝나고 순열 하나를 저장했다면
                used[i] = False
                path.pop()

            return
        backtracking()

        return result
