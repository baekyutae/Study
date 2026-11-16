class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        '''
        좌측항의 합과 우측항의 합을 구해서 둘이 더해 result에 넣어야함
        left_part =  i*nums[i] - left_sum(좌항의 원소 전체합)
        right_part = right_sum - (n-1-i)*nums[i]

        left_sum = 왼쪽부터 스캔할시 순차적으로 nums[0] 부터 더해감
        right_sum = total - left_sum

        n-1-i = 우항의 원소 갯수, 1은 nums[i]자기자신  i는 좌항의 원소 갯수 n은 전체 개수
        n = len(nums)
        '''
        result = []
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            left_part =  i*nums[i] - left_sum
            right_sum = total-left_sum-num # 우항의 원소 총합을 구해
            right_part = right_sum - (n-1-i)*nums[i] # 거기다 우항의 갯수*nums[i] 를 뺌
            left_sum += num

            result.append(left_part+right_part)

        return result
