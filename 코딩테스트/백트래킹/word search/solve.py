class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            # word의 모든 글자를 찾음
            if index == len(word):
                return True

            # 보드 범위를 벗어남
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            # 현재 칸이 필요한 글자와 다름
            if board[row][col] != word[index]:
                return False

            # 현재 경로에서 이 칸을 다시 사용하지 못하도록 방문 처리
            original = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # 다른 경로에서 사용할 수 있도록 원상복구
            board[row][col] = original

            return found

        # 모든 칸을 시작점 후보로 확인
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False