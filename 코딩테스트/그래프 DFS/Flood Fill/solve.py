from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])

        visited = set()
        original_color = image[sr][sc]

        # 인접 픽셀 탐색 및 변환 함수
        def change(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return

            if (r, c) in visited or image[r][c] != original_color:
                return

            visited.add((r, c))
            image[r][c] = color

            return change(r + 1, c), change(r - 1, c), change(r, c + 1), change(r, c - 1)

        change(sr, sc)
        return image
