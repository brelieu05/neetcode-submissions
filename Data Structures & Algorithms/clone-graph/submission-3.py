"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(curr): # return cloned node
            if curr in oldToNew:
                return oldToNew[curr]

            clone = Node(curr.val)
            oldToNew[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone
            
        
        return dfs(node) if node else None

