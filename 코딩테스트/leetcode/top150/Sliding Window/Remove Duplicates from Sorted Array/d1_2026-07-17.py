class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 새숫자 넣을 위치, 맨앞 0위치는 차피 중복 여부와 무관하니 1부터 시작
        input = 1

        # 숫자 탐색 시작, 마찬가지 이유로 1부터 시작
        for number in range(1, len(nums)):
            if nums[number] > nums[number-1]:
                nums[input] = nums[number]
                input += 1

        # 새숫자를 넣을 인덱스가 곧 중복이 제거된 숫자 배열의 길이 k와 동일
        return input
