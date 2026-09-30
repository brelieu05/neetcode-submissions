# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))

        def dfs(node):
            nonlocal res

            if not node:
                return

            left = getHeight(node.left)
            right = getHeight(node.right)

            
            dfs(node.left)
            dfs(node.right)
            res = max(res, left + right)


        res = 0
        dfs(root)
        return res