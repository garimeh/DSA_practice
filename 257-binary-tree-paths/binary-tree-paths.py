# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(node, path):
            npath = path + str(node.val)
            if not node.left and not node.right:
                self.res.append(npath)
                return
            else:
                npath = npath + '->'
                if node.left:
                    helper(node.left, npath)
                if node.right:
                    helper(node.right, npath)
            return
        path = ''
        if not root:
            return []
        helper(root, path)
        return self.res