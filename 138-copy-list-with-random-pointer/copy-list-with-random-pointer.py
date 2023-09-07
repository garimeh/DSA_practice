"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        hmp = {}
        while cur:
            hmp[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            hmp[cur].next = hmp.get(cur.next)
            hmp[cur].random = hmp.get(cur.random)
            cur = cur.next
        return hmp[head]