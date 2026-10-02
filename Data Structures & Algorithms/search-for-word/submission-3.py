class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(r, c, curr, path):
            if curr == word:
                return True

            if (r, c) in path or r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False

            curr += board[r][c]
            path.add((r, c))
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, curr, path):
                    return True
            path.remove((r,c))
            curr = curr[:-1]

            return False

            

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, "", set()):
                    return True

        return False