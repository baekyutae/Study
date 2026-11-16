class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        # 현재 탐색하는 좌표와, 찾아야할 word[i]를 인자로 사용
        def backtracking(r,c,i):

            if len(word) == i:
                return True
            
            if not (0<=r<row and 0<=c<col):
                return False

            if board[r][c] != word[i]:
                return False

            
            # 현재 탐색하는 단어를 체크표시
            save = board[r][c]
            board[r][c] = "#"

            # 상하좌우로 탐색 
            check = (backtracking(r+1,c,i+1) or backtracking(r-1,c,i+1) 
                     or backtracking(r,c+1,i+1) or backtracking(r,c-1,i+1))

            board[r][c] = save

            return check

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtracking(r,c,0):
                        return True

        return False
