class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        r_top = 0
        r_bottom = len(matrix) - 1
        c_left = 0
        c_right = len(matrix[0]) - 1

        while r_top <= r_bottom and c_left <= c_right:
            # 1. top row
            for j in range(c_left, c_right + 1):
                ans.append(matrix[r_top][j])
            r_top += 1

            # 2. right column
            for i in range(r_top, r_bottom + 1):
                ans.append(matrix[i][c_right])
            c_right -= 1

            # 3. bottom row
            if r_top <= r_bottom:
                for j in range(c_right, c_left - 1, -1):
                    ans.append(matrix[r_bottom][j])
                r_bottom -= 1

            # 4. left column
            if c_left <= c_right:
                for i in range(r_bottom, r_top - 1, -1):
                    ans.append(matrix[i][c_left])
                c_left += 1

        return ans