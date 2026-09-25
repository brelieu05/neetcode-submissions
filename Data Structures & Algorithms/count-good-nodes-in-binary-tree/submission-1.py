# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, float('-inf'))])

        while q:
            node, upper = q.popleft()

            if not node:
                continue

            if node.val >= upper:
                res += 1
            
            q.append((node.left, max(upper, node.val)))
            q.append((node.right, max(upper, node.val)))

        return res




            