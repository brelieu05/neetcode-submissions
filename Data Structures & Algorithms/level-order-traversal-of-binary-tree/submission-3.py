# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        stack = [(root, 0)]
        
        while stack:
            node, depth = stack.pop()

            if not node:
                continue

            if depth == len(res):
                res.append([])
        
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))
            res[depth].append(node.val)

        return res