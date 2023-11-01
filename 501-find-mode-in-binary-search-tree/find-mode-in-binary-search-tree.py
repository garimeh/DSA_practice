# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 
            freq[node.val] = freq.get(node.val, 0) + 1
            l = dfs(node.left)
            r = dfs(node.right)

        freq = {}
        dfs(root)
        m = max(freq.values())
        ans = []
        for k,v in freq.items():
            if v == m:
                ans.append(k)
        return ans