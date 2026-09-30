# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while True:
            if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
                return root
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                root = root.left
