from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        next_level = deque([root,])

        while next_level:
            curr = next_level
            next_level = deque()

            for node in curr:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return sum([node.val for node in curr])
        
# Results: Time 98.56% (184ms) space 22.58% (17.8MB)