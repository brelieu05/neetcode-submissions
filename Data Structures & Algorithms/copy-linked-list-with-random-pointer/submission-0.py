"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_map = {}
        
        def dfs(node):
            if not node:
                return None

            if node in nodes_map:
                return nodes_map[node]

            clone = Node(node.val)
            nodes_map[node] = clone
            clone.next = dfs(node.next)
            clone.random = nodes_map.get(node.random)
            return clone

        return dfs(head)
            

            