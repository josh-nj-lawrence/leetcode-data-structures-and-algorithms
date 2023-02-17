from typing import Optional
from tools.linkedlists import dListNode, print_list, build_ll
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    
sol = Solution()
lst1 = build_ll([1,1,2])
print_list(sol.deleteDuplicates(lst1))
lst2 = build_ll([1,1,2,3,3])
print_list(sol.deleteDuplicates(lst2))

# Results: time 81.14% (41ms) 21.62% space (13.9MB) 