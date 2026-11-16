class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 수송능력을 매개변수로 받아 수송에 걸리는 날짜를 반환
        def dayCheck(carry):
            # count는 1부터 시작: 무조건 하루는 운송을 하니깐
            count = 1
            # 하루 수송 가능량 cur_carry에서 weights의 원소 weight를 빼다 남은 수송량이 weight 보다 작아지면 하루 갱신하고 수송 가능량 cur_carry =  carry로 갱신
            cur_carry = carry

            for weight in weights:
                if cur_carry >= weight:
                    cur_carry -= weight
                else:
                    cur_carry = carry
                    cur_carry -= weight
                    count += 1

            return count

        # max(weights) -> weights의 최대 무게는 최소한 수송 가능해야함
        # sum(weights) -> 하루만에 모든 화물을 옮길수 있는 최대 값
        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if dayCheck(mid) <= days:
                hi = mid

            else:
                lo = mid + 1

        return lo
