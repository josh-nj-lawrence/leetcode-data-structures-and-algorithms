from typing import Optional
from tools.linkedlists import build_ll, print_list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            Need to work backwards from right to left, keep pointer to left-1 and right+1
        """
        # Deal with null and 1 node cases
        if not head: 
            return head
        if head.next == None:
            return head
        if left == right:
            return head
        # Itterate over whole list until we reach right+1
        curr = head
        prev = None
        nextNode = head
        for i in range(right+1):
            # Should process the left = 1 case
            if i == left-1:
                l_node = nextNode#curr.next
                prev_l_node = curr
                prev = curr
            if i == right:
                r_node = curr
                if prev_l_node: 
                    prev_l_node.next = r_node # Link previous segment to rev
                next_r_node = curr.next
                l_node.next = next_r_node # Link rev segment to posterier segment
                r_node.next = prev
                prev = curr
            if i >= left and i < right:
                # Reverse node
                curr.next = prev
                prev = curr
                curr = nextNode

            curr = nextNode #curr.next
            if curr:
                nextNode = curr.next
        return head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int):
        # base case
        if 
    def recurse(self, m: int, n: int, right: Optional[ListNode]):
        
sol = Solution()
lst1 = build_ll([3,5])
print_list(sol.reverseBetween(lst1, 1, 2))