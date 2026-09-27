class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def backtracking(r,c,idx):
            if idx == len(word):
                return True

            if not (0<=r<row  and 0<=c<col):
                return False

            if board[r][c] != word[idx]:
                return False

            board[r][c] = "#"

            found = (backtracking(r+1,c,idx+1) 
            or backtracking(r-1,c,idx+1)
            or backtracking(r,c+1,idx+1)
            or backtracking(r,c-1,idx+1))

            board[r][c] = word[idx]

            return found

        for r in range(row):
            for c in range(col):
                if backtracking(r,c,0):
                    return True
                
        return False
