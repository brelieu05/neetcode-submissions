# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(root, 0)]

        # def dfs(node, depth):
        #     if not node:
        #         return

        #     if depth == len(res):
        #         res.append(node.val)

        #     if node:
        #         dfs(node.right, depth + 1)
        #         dfs(node.left, depth + 1)
        # dfs(root, 0)

        while stack:
            node, depth = stack.pop()

            if node:
                if depth == len(res):
                    res.append(node.val)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))


        return res