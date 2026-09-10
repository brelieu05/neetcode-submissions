class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        directions  = ((0, 1), (0, -1), (-1, 0), (1, 0))
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0


        def bfs(r, c) -> int:
            newArea = 0

            while q:
                qr, qc = q.popleft()
                newArea += 1

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return newArea



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    q.append((r, c))
                    visited.add((r, c))
                    currArea = bfs(r, c)
                    maxArea = max(maxArea, currArea)

        return maxArea