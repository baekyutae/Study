'''
1차원 index에서 2차원 좌표를 찾는 방식

row = index // col_count
col = index % col_count

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)*len(matrix[0]) - 1
        n = len(matrix[0])
        while left <= right:
            mid = (left+right)//2
            number = self._mid_number(matrix, mid, n)
            if number == target:
                return True

            elif number < target:
                left = mid+1

            else:
                right = mid - 1

        return False

    def _mid_number(self, matrix, mid, n):
        x = mid //n
        y = mid % n

        return matrix[x][y]