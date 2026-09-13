class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        visited, cycle = set(), set()
        res = []

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(node):
            if node in cycle:
                return False

            if node in visited:
                return True

            cycle.add(node)
            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            res.append(node)

            return True
                


        for i in range(numCourses):
            if not dfs(i):
                return []

        return res