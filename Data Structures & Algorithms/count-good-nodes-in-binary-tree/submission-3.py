# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # stack = [(root, float('-inf'))]

        # while stack:
        #     node, upper = stack.pop()

        #     if not node:
        #         continue

        #     if node.val >= upper:
        #         res += 1
            
        #     stack.append((node.right, max(upper, node.val)))
        #     stack.append((node.left, max(upper, node.val)))

        def dfs(node, upper):
            nonlocal res

            if not node:
                return
            
            if node.val >= upper:
                res += 1
            
            dfs(node.right, max(upper, node.val))
            dfs(node.left, max(upper, node.val))

        dfs(root, float('-inf'))
        return res




            