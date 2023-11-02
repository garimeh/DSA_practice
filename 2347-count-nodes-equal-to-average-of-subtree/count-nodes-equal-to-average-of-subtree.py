# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            nonlocal ans
            if not node:
                return (0,0)

            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == (l[0] + r[0] + node.val)//(l[1] + r[1] + 1):
                ans += 1

            return (l[0] + r[0] + node.val, l[1] + r[1] + 1)

        ans = 0
        dfs(root)
        return ans