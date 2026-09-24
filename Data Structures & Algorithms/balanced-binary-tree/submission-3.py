# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))

        def dfs(node):
            if not node:
                return True

            left = getHeight(node.left)
            right = getHeight(node.right)

            if abs(left - right) >= 2:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)