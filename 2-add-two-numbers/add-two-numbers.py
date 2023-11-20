# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        p = l1
        q = l2
        current = dummy_head
        carry = 0

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            if p is not None: 
                p = p.next
            if q is not None: 
                q = q.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next