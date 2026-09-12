class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        adj = {i : [] for i in range(1, len(edges) + 1)}
        visited = set()
        res = []

        def dfs(node, parent):
            if visit[node]:
                return True
            
            visit[node] = True

            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False


        for curr, out in edges:
            adj[curr].append(out)
            adj[out].append(curr)
            visit = [False] * (len(edges) + 1)

            if dfs(curr, -1):
                return [curr, out]

        return []