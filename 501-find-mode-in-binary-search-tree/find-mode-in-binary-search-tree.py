from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        freq = {}
        while q:
            node = q.popleft()
            freq[node.val] = freq.get(node.val, 0) + 1
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        m = max(freq.values())
        ans = []
        for k,v in freq.items():
            if v == m:
                ans.append(k)
        return ans