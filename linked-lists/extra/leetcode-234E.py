from tools.linkedlists import build_ll, ListNode
from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        if head.next is None:
            return True
                
        first_half_end = self.first_half_end(head)
        second_half_start = self.reverse_ll(first_half_end.next)

        ans = True
        p1,p2 = head, second_half_start
        while ans and p2 is not None:
            if p1.val != p2.val:
                ans = False
            p1, p2 = p1.next, p2.next
        
        return ans

    def reverse_ll(self, head):
        prev = None
        curr = head
        nextNode = curr.next
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
    
    def first_half_end(slef, head):
        slow,fast = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

lst = build_ll([1,2,2,1,3])
sol = Solution()
print(sol.isPalindrome(lst))

# Results: 11.16% (1342ms) 74.59% space (39MB)