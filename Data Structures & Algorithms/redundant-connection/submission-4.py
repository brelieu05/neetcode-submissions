class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i : [] for i in range(1, n + 1)}
        
        def dfs(node, parent, visited):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node, visited):
                    return False
            return True

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if not dfs(u, v, visited):
                return [u, v]

        return []