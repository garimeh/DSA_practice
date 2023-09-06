# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        base_size, extra = divmod(n, k)
        
        ans = []
        cur = head
        
        # Create k parts
        for i in range(k):
            # Initialize the dummy node and current node for this part
            dummy = ListNode(0)
            part_cur = dummy
            # Create the part list
            for j in range(base_size + (i < extra)):
                part_cur.next = cur
                part_cur = part_cur.next
                cur = cur.next
            # End the part list
            if part_cur:
                part_cur.next = None
            ans.append(dummy.next)
        
        return ans