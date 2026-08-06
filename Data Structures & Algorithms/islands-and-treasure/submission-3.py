class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                for dr, dc in directions:
                    if not (0 <= r + dr < ROWS and 0 <= c + dc < COLS) or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == -1:
                        continue
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            dist += 1




            

                