class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        path = set()
        
        def backtrack(r, c, index):
            if index + 1 == len(word):
                return True

            path.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in path and board[nr][nc] == word[index + 1]:
                    if backtrack(nr, nc, index + 1):
                        return True
            path.remove((r,c))
            return False

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False

            