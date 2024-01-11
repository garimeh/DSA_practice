# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def vals(node, minval, maxval):
            if not node:
                return 
            self.diff = max(self.diff, max(abs(minval - node.val), abs(maxval - node.val)))
            minval = min(minval, node.val)
            maxval = max(maxval, node.val)
            vals(node.left, minval, maxval)
            vals(node.right, minval, maxval)
        minval = root.val
        maxval = root.val
        vals(root, minval, maxval)
        return self.diff