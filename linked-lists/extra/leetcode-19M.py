from tools.linkedlists import build_ll, ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        n_behind = dummy
        curr = dummy

        if head.next == None:
            return None
        # Move curr ahead of n_behind
        for _ in range(n+1):
            curr = curr.next

        while curr:
            curr = curr.next
            n_behind = n_behind.next

        n_behind.next = n_behind.next.next
        return dummy.next

lst1 = build_ll([1,2,3,4,5])
sol = Solution()
print(sol.removeNthFromEnd(lst1,2))

# Results: 52.74% time (37ms) 60.32% space (13.8MB)