# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l_height = self.maxDepth(root.left)
            r_height = self.maxDepth(root.right)
            return max(l_height, r_height) + 1


three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven

sol = Solution()
print(sol.maxDepth(three))

# Results: 40.76% time (47ms) 18.61% space (16.3MB)