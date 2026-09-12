class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = set()
        q = deque()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                qr, qc = q.popleft()

                grid[qr][qc] = dist

                for dr, dc in directions:
                    nei_row, nei_col = qr + dr, qc + dc

                    if 0 <= nei_row < ROWS and 0 <= nei_col < COLS and (nei_row, nei_col) not in visited and grid[nei_row][nei_col] > 0:
                        q.append((nei_row, nei_col))
                        visited.add((nei_row, nei_col))
            dist += 1





            