class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        minutes = 0

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        
        while q:
            for i in range(len(q)):
                qr, qc = q.popleft()

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            minutes += 1


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes - 1 if minutes > 0 else 0