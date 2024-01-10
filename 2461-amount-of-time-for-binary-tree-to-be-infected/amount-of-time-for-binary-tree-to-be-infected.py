# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxd = 0
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            d = 0
            if not node:
                return d
            r = dfs(node.right)
            l = dfs(node.left)
            if node.val == start:
                self.maxd = max(l, r)
                d = -1
            elif l>=0 and r >=0:
                d = max(l,r) + 1
            else:
                dist = abs(l) + abs(r)
                self.maxd = max(self.maxd, dist)
                d = min(l,r) - 1
            return d
        dfs(root)
        return self.maxd