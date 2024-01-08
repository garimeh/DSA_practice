# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], lo: int, hi: int) -> int:
        # sum = 0
        def help(node):
            if not node:
                return 0
            return node.val + help(node.left) + help(node.right) if lo <= node.val <= hi else help(node.left) + help(node.right)

        return help(root)  