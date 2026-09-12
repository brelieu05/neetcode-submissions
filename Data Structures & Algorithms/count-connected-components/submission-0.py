class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        visited = set()
        res = 0

        for curr, out in edges:
            adj[curr].append(out)
            adj[out].append(curr)

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                if node == parent:
                    continue
                dfs(nei, node)


        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1

        return res
