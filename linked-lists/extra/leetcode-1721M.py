from tools.linkedlists import build_ll, ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        fast, slow = head, head
       
        # Seperate fast and slow by k nodes
        for _ in range(k-1): 
            fast = fast.next
        dummy = fast

        # Itterate to the end to grab the n-kth node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Swap the nodes values
        dummy.val, slow.val = slow.val, dummy.val

        return head

sol = Solution()
lst1 = build_ll([7,9,6,6,7,8,3,0,9,5])
print(sol.swapNodes(lst1, 5))

# Results: 59.86% time (1044ms) 48.50% space(48.4MB)