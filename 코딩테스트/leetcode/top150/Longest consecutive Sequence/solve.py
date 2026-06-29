class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set 자료형을 활용해  연속되는 숫자가 있는지 여부를 확인함
        # 있으면 1씩 더해가며 해시맵에 들어있는지 체크 => 안나올때 까지 반복
        set_nums = set(nums)
        longest_streak = 0
        for number in set_nums:
            if number-1 not in set_nums:
                current_num = number
                currnet_streak = 1
                
                while current_num + 1 in set_nums:
                    current_num += 1
                    currnet_streak += 1

                longest_streak = max(longest_streak, currnet_streak)

        return longest_streak