from collections import deque
from typing import Optional, List 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        row = [root.val]
        ans =[]
        while queue:
            ans.append(max(row))
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            row = [node.val for node in queue]
        return ans
    
# Results: time 84.71% (44ms) space 94.71% (16.2MB) 