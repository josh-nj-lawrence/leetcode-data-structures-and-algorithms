from tools.linkedlists import build_ll, ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            if head.val == val:
                return None
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        
        prev = sentinel
        curr = head
        
        while curr:
            if curr.val == val:
                try:
                    prev.next = curr.next
                except AttributeError:
                    prev.next = None
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return sentinel.next
    
lst = build_ll([1])
sol = Solution()
print(sol.removeElements(lst,1))

# Results: 18.88% time (83ms) 94.4% space (17.3MB)