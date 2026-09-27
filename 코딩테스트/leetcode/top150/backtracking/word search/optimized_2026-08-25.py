from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        # board에 word 글자가 필요한 개수만큼 있는지 먼저 확인
        board_count = Counter(ch for line in board for ch in line)
        word_count = Counter(word)
        for ch, need in word_count.items():
            if board_count[ch] < need:
                return False

        # 시작점 후보가 더 적은 쪽에서 출발하도록 방향 결정
        if board_count[word[-1]] < board_count[word[0]]:
            word = word[::-1]

        def backtracking(r, c, i):
            # i가 곧 지금까지 맞춘 글자 수라 path가 필요없다
            if i == len(word):
                return True

            if not (0 <= r < row and 0 <= c < col):
                return False

            # "#"은 word에 없는 문자라 방문 검사도 이 비교가 겸한다
            if board[r][c] != word[i]:
                return False

            save = board[r][c]
            board[r][c] = "#"

            # 조건식 안에서 직접 호출해 첫 성공에서 즉시 중단
            found = (backtracking(r + 1, c, i + 1)
                     or backtracking(r - 1, c, i + 1)
                     or backtracking(r, c + 1, i + 1)
                     or backtracking(r, c - 1, i + 1))

            board[r][c] = save

            return found

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0] and backtracking(r, c, 0):
                    return True

        return False
