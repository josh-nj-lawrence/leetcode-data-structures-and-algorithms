from tools.linkedlists import build_ll, print_list
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find middle of array with fast/slow
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Now slow points to the left-middle node. 

        # Reverse second half
        prev = None
        curr = slow
        nextNode = slow
        while curr:
            nextNode = nextNode.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # Prev stores second half head

        # Find max twosum
        ans = 0
        n1, n2 = head, prev
        while n1 and n2:
            ans = max(ans, (n1.val + n2.val))
            n1 = n1.next
            n2 = n2.next
        return ans

lst1 = build_ll([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
sol = Solution()
print(sol.pairSum(lst1))

# Results: 57.42% time (978 ms) 73.73% space (45.1 MB)