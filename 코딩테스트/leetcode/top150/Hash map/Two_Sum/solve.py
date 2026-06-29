'''
현재 숫자 v를 본다
target을 만들기 위해 필요한 숫자 need = target - v를 구한다
need가 이전에 나온 적 있으면 정답
없으면 현재 숫자를 seen에 저장

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, v in enumerate(nums):
            need = target - v

            if need in seen:
                return [seen[need],i]

            seen[v] = i