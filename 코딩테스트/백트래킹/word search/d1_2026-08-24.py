class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        # 탐색 경로 저장
        path = []

        # 탐색 함수
        def backtracking(r,c,i):
            if len(path) == len(word):
                return True

            if not (0<=r<row and 0<=c<col):
                return False

            if board[r][c] == "#" or word[i] != board[r][c] :
                return False


            # 방문 처리
            path.append(board[r][c])
            save = board[r][c]
            board[r][c] = "#"

            # 상하좌우 탐색
            up = backtracking(r-1,c,i+1)
            down = backtracking(r+1,c,i+1)

            left = backtracking(r,c+1,i+1)
            right = backtracking(r,c-1,i+1)

            # 탐색한 좌표를 되돌리기
            path.pop()
            board[r][c] = save

            return up or down or left or right


        # board를 순회하며 탐색 함수 실행
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtracking(r,c,0):
                        return True

        return False
