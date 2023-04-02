from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS where last element in queue appends to ans
        if root is None:
            return []
        queue = deque([root])
        ans = []
        while queue:
            curr = queue
            queue = deque()
            while curr:
                node = curr.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        return ans
    
#Results: time 64.26% (34ms) space 58.37% (13.8MB) 