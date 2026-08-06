class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addRoom(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])


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
                    addRoom(r + dr, c + dc)

            dist += 1

            