class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        visited = set() # not keeping track of all visited, just our current path

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs) -> bool: # show if it has a valid course path that is completely finishable
            if crs in visited:
                return False
            
            if adj[crs] == []:
                return True

            visited.add(crs)
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            adj[crs] = []

            return True
            

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        




    
        