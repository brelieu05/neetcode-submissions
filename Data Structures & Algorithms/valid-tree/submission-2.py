class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        preMap = [[] for _ in range(n)]

        for node1, node2 in edges:
            preMap[node1].append(node2)
            preMap[node2].append(node1)

        visit = set()

        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)

            for pre in preMap[node]:
                if pre == par:
                    continue
                if not dfs(pre, node):
                    return False
            return True


        return dfs(0, -1) and len(visit) == n

