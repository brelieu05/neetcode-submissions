class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                qr, qc = q.popleft()
                grid[qr][qc] = dist

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1
                