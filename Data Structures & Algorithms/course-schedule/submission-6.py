class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        visited, cycle = set(), set()

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visited:
                return True
            
            cycle.add(crs)

            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        




    
        