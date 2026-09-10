class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (r, c)
        q = deque() # (r, c)
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        

        def bfs(r, c):
            
            while q:
                qr, qc = q.popleft()

                # check in every direction
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                    


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    visited.add((r, c))
                    q.append((r, c))
                    bfs(r, c)
                    islands += 1
                
        return islands