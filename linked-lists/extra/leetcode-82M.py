from tools.linkedlists import ListNode, build_ll
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head

        prev = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skipp over dups
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return sentinel.next
        
sol = Solution()
lst1 = build_ll([1,2,3,3,3,3,4])
print(lst1)
print(sol.deleteDuplicates(lst1))

# Results: 59.54% time (44 ms) 21.61% space (14MB)