# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(curr, last):
            nonlocal res

            if not curr:
                return
                
            if curr.val >= last:
                res += 1
            
            dfs(curr.left, max(last, curr.val))
            dfs(curr.right, max(last, curr.val))

        dfs(root, root.val)
        return res
            