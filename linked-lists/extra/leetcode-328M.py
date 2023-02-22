from tools.linkedlists import build_ll, ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        p1,p2, first_p2 = head, head.next, head.next
        while p1.next.next and p2.next.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        # When we reach here we need to determine which element failed to ensure we tie the list together
        if p1.next.next:
            p1.next = p1.next.next
            p1 = p1.next
            p2.next = None
        p1.next = first_p2
        return head
    
sol = Solution()
lst = build_ll([1,2,3,4,5,6,7])
print(sol.oddEvenList(lst))

# Results: 11.71% time (72ms) 68.4% space (16.5 MB)