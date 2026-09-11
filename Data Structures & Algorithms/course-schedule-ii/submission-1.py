class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        visited = set()
        res = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            
            if adj[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            
            visited.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            adj[crs] = []
            
            if crs not in res:
                res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res