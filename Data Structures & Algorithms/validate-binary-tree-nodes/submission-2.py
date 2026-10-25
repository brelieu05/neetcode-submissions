class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        connections = defaultdict(list)

        for i in range(n):
            if i not in connections:
                connections[i] = [0, 0] # indegree, outdegree
            if leftChild[i] != -1 and leftChild[i] not in connections:
                connections[leftChild[i]] = [0, 0]
            if rightChild[i] != - 1 and rightChild[i] not in connections:
                 connections[rightChild[i]] = [0, 0]

            if leftChild[i] != -1:
                connections[leftChild[i]][0] += 1
                connections[i][1] += 1

            if rightChild[i] != - 1:
                connections[rightChild[i]][0] += 1
                connections[i][1] += 1
    
        # find root

        roots = []
        for i, v in connections.items():
            indegree, outdegree = v

            if indegree == 0:
                roots.append(i)

        if len(roots) > 1:
            return False



        visited = set()

        while roots:
            node = roots.pop()

            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                roots.append(leftChild[node])
            if rightChild[node] != -1:
                roots.append(rightChild[node])


        return len(visited) == n
                
                
