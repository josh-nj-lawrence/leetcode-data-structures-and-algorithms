# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode) -> int:
            # Diameter at any node is len of longest path on left + right
            # Return longest path on left or right
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.ans = max(self.ans, left+right)
            return max(left,right)
        helper(root)
        return self.ans
        
# Results: 72.79% time (45ms) 97.90% space (16.2 MB)
