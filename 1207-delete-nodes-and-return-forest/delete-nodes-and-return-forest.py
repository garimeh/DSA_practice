# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        fors = []
        dels = set(to_delete)
        def dfs(node):
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)

            if node.val in to_delete:
                if node.left:
                    fors.append(node.left)
                if node.right:
                    fors.append(node.right)
                return None
            return node
        res = dfs(root)
        if res:
            fors.append(res)  
        return fors