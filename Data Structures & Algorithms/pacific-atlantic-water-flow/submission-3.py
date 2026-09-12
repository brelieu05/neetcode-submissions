class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()

        pac = set()
        atl = set()

        res = []

        def dfs(r, c, ocean):
            if r < 0 or r > ROWS or c < 0 or c > COLS or (r, c) in ocean:
                return
            
            ocean.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, ocean)


        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS - 1, atl)

        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS - 1, c, atl)

        for r in range(ROWS):
            for c in range(COLS):
                q.append((r, c))
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res