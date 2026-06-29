'''
회전 배열에서는 mid 기준으로 한쪽은 반드시 정렬되어 있다.
정렬된 쪽에 target이 있으면 그쪽으로 가고,
없으면 반대쪽으로 간다.


while 탐색 구간이 남아있으면:

    mid 확인

    target 찾았으면 반환

    왼쪽이 정렬되어 있으면:
        target이 왼쪽 범위 안에 있나?
            맞으면 오른쪽 버림
            아니면 왼쪽 버림

    오른쪽이 정렬되어 있으면:
        target이 오른쪽 범위 안에 있나?
            맞으면 왼쪽 버림
            아니면 오른쪽 버림

못 찾으면 -1

시간 복잡도: O(log n)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 절반이 정렬된 경우
            if nums[left] <= nums[mid]:
                # target이 왼쪽 정렬 구간 안에 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # 오른쪽 절반이 정렬된 경우
            else:
                # target이 오른쪽 정렬 구간 안에 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1