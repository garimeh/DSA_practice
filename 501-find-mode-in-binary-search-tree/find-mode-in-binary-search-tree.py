# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        @cache
        def dfs(node):
            nonlocal prevnum, curstreak, maxstreak, ans 
            if not node:
                return 
            dfs(node.left)
            if node.val == prevnum:
                curstreak += 1
            else:
                prevnum = node.val
                curstreak = 1
            if maxstreak < curstreak:
                ans = []
                maxstreak = curstreak
            if curstreak == maxstreak:
                ans.append(node.val)

            dfs(node.right)
        ans, prevnum, maxstreak, curstreak =[], -1, 0 , 0
        dfs(root)
        return ans