from typing import Optional
from typing import defaultdict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = defaultdict(int)
        # Itter over list
        while head:
            if seen[head] == 1:
                return True
            seen[head] = 1
            head = head.next
        return False

# Results: 39.41% time (63 ms) 8.76% space (18MB)