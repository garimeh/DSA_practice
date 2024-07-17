# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root :
            return []
        dels = set(to_delete)
        fors = []
        q = [root]
        while q:
            curnode = q.pop(0)
            if curnode.left:
                q.append(curnode.left)
                if curnode.left.val in dels:
                    curnode.left = None
            if curnode.right:
                q.append(curnode.right)
                if curnode.right.val in dels:
                    curnode.right = None
            if curnode.val in dels:
                if curnode.left:
                    fors.append(curnode.left)
                if curnode.right:
                    fors.append(curnode.right)
        if root.val not in dels:
            fors.append(root)
        return fors