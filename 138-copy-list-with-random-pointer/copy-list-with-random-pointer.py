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
        cur = head
        while cur:
            curn = cur.next
            cur.next = Node(cur.val)
            cur.next.next = curn
            cur = curn
        
        cur = head
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        dummy = Node(0)
        copy = dummy
        while cur:
            front = cur.next.next
            copy.next = cur.next
            cur.next = front
            copy = copy.next
            cur = cur.next
        return dummy.next