from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        row = deque([root])
        ans = []
        dir_flag = True

        while row:
            curr = len(row)
            #Append to answer array
            if dir_flag:
                # append left -> right
                ans.append([node.val for node in row])
                dir_flag = False
            else:
                ans.append([node.val for node in reversed(row)])
                dir_flag = True
            # Add next row
            for _ in range(curr):
                node = row.popleft()
                if node.left:
                    row.append(node.left)
                if node.right:
                    row.append(node.right)
        return ans

# Results: time 36.76% (38ms) space 47.33%

