# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(set)
        stack = [root]
        while stack:
            cur = stack.pop(0)
            if cur.left: 
                stack.append(cur.left)
                adj[cur.val].add(cur.left.val)
                adj[cur.left.val].add(cur.val)
            if cur.right:
                stack.append(cur.right)
                adj[cur.val].add(cur.right.val)
                adj[cur.right.val].add(cur.val)
        
        vis = {start}
        q = deque([start])
        ans = 0
        while q:
            lev = len(q)
            while lev > 0:
                cur = q.popleft()
                for num in adj[cur]:
                    if num not in vis:
                        vis.add(num)
                        q.append(num)
                lev -= 1
            ans += 1
        return ans - 1