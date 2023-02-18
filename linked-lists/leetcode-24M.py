from tools.linkedlists import ListNode, dListNode, print_list, build_ll
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy

        while head and head.next:
            first_node = head
            second_node = head.next
            # Swapping
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next
        # Return the new head node.
        return dummy.next
    
sol = Solution()
lst1 = build_ll([1,2,3,4,5,6,7,8,9])
print_list(sol.swapPairs(lst1))

# Results: 86.84% time (29ms) 55.82% space (13.9MB)