class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = {i : [] for i in range(numCourses)} # crs : []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(crs):
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


        for crs in range(numCourses):
            if not dfs(crs):
                return False
                


        return True