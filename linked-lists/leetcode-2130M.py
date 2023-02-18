from tools.linkedlists import build_ll, print_list
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        og_head = head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Now slow points to the left-middle node. Reverse second half
        prev = None
        curr = slow
        nextNode = slow.next
        while curr.next:
            curr.next = prev
            prev = curr
            curr = nextNode
            nextNode = curr.next
        
        slow.next = curr
        return og_head

lst1 = build_ll([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
sol = Solution()
print_list(sol.pairSum(lst1))

#   p
#     c
#       n
# 0,1,2,3,4