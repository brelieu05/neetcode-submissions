class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (r, c)
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque() # (0, 1)
        res = 0
        possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    q.append((r, c))
                    visited.add((r, c))

                    while q:
                        q_row, q_col = q.popleft()

                        
                        for dr, dc in possible_directions:
                            if 0 <= q_row + dr < ROWS and 0 <= q_col + dc < COLS and (q_row + dr, q_col + dc) not in visited and grid[q_row + dr][q_col + dc] == "1":
                                q.append((q_row + dr, q_col + dc))
                                visited.add((q_row + dr, q_col + dc))
                elif (r, c) not in visited:
                    visited.add((r, c))
                        
        



        return res