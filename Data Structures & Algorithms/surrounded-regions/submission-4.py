class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        q = deque()

        for r in range(ROWS):
            q.append((r, 0))
            q.append((r, COLS - 1))

        for c in range(COLS):
            q.append((0, c))
            q.append((ROWS - 1, c))

        while q:
            r, c = q.popleft()
            if board[r][c] != "O":
                continue

            board[r][c] = "A"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    q.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "A":
                    board[r][c] = "O"
                    
