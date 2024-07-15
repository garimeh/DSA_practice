# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        childs = set()
        for par, chi, l in descriptions:
            childs.add(chi)
            if par not in tree:
                tree[par] = TreeNode(par)
            if chi not in tree:
                tree[chi] = TreeNode(chi)
            if l:
                tree[par].left = tree[chi]
            else:
                tree[par].right = tree[chi]
        root = None
        for a in tree.values():
            if a.val not in childs:
                return a
        return None