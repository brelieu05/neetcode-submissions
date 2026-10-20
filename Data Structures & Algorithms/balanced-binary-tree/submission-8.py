# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if not root:
                return 0

            left = getHeight(root.left)
            right = getHeight(root.right)

            return 1 + max(left, right)

        def dfs(root):
            if not root:
                return True

            left = dfs(root.left)
            right = dfs(root.right)

            if abs(getHeight(root.left) - getHeight(root.right)) > 1:
                return False
            
            return left and right
            
        return dfs(root)