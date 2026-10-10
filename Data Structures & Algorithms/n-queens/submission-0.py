class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        queen_locations = []
        res = []

        def safe(r, c):
            nr, nc = r, c
            for q in queen_locations:
                if q[0] == r or q[1] == c or abs(q[0] - r) == abs(q[1] - c):
                    return False
                
            return True
        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in grid])
                return 

            for c in range(n):
                if safe(r, c):
                    grid[r][c] = "Q"
                    queen_locations.append((r, c))
                    backtrack(r + 1)
                    queen_locations.pop()
                    grid[r][c] = "."



        backtrack(0)
        return res