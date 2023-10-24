from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            cursize = len(q)
            maxval = float('-inf')

            for _ in range(cursize):
                node = q.popleft()
                maxval = max(maxval, node.val)

                for c in [node.left, node.right]:
                    if c:
                        q.append(c)
            ans.append(maxval)
        return ans