# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            return False

        def dfs(node, subnode):
            if not node:
                return False
                
            if isSameTree(node, subnode):
                return True


            
            
            return dfs(node.left, subnode) or dfs(node.right, subnode)

        return dfs(root, subRoot)
        

