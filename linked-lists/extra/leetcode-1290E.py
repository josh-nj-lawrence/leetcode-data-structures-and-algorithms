from tools.linkedlists import build_ll, ListNode
from typing import Optional, List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res

lst = build_ll([1,0,0,1])
sol = Solution()
print(sol.getDecimalValue(lst))

# Results: Submission 1: 11.36% time (45ms) 5.58% space (13.9MB)
# Submission 2: 15.16% time (42ms) 94.35% space (13.7MB)
# Submission 3: 98.88% time (22ms) 5.58% space (13.9MB)