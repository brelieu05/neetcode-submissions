class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        ROWS = len(heights)
        COLS = len(heights[0])

        pac = [[False for c in range(COLS)] for r in range(ROWS)]
        atl = [[False for c in range(COLS)] for r in range(ROWS)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                qr, qc = q.popleft()
                ocean[qr][qc] = True

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[qr][qc] <= heights[nr][nc] and not ocean[nr][nc]:
                        q.append((nr, nc))


        pacific = []
        atlantic = []

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])


        return res

        