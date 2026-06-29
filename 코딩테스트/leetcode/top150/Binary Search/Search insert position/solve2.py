# Search Insert Position 핵심 원리
#
# while left <= right 이진 탐색이 끝나면 항상 left > right 상태가 된다.
# 보통은 left == right + 1 상태로 종료된다.
#
# 이때 left의 의미:
#   target보다 작은 값들이 끝난 바로 다음 위치
#   == target 이상인 값이 처음 시작되는 위치
#   == target을 삽입해도 정렬이 유지되는 위치
#
# 반복 중 유지되는 불변식:
#   nums[0:left]      -> 전부 target보다 작다고 확정된 구간
#   nums[right+1:]    -> 전부 target보다 크거나 같다고 확정된 구간
#
# nums[mid] < target 이면:
#   mid 이하 값들은 전부 target보다 작으므로 left = mid + 1
#
# nums[mid] > target 이면:
#   mid 이상 값들은 target보다 크므로 right = mid - 1
#
# 따라서 target을 못 찾고 반복문이 끝나도
# left가 곧 target이 들어갈 정답 인덱스가 된다.

# 시간 복잡도 logn


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) -1 


        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            elif nums[mid]<target:
                left= mid+1

            else:
                right = mid - 1

        return left