"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        while node:
            if node.child:
                nex = node.next
                node.next = node.child
                node.next.prev = node
                node.child = None
                p = node.next
                while p.next:
                    p = p.next
                p.next = nex
                if nex: nex.prev = p
            node = node.next
        return head
