from tools.linkedlists import build_ll, print_list
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = head
        if head.next == None:
            return None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        slow.next = None
        return head

lst1 = build_ll([1])
sol = Solution()
print_list(sol.deleteMiddle(lst1))

# Results: 77.7% time (1792ms) 11.67% space (60.8MB)
        