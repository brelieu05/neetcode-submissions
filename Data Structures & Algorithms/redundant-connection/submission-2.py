class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(1, len(edges) + 1)}

        
        def dfs(node, parent, visited):
            if node in visited:
                return True

            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node, visited):
                    return True

            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()
            if dfs(u, -1, visited):
                return [u, v]

        return []