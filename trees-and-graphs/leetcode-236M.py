# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode') -> bool:
            if not node:
                # Leaf node
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)

            mid = node == p or node == q

            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        dfs(root)
        return self.ans


# Results: 57.37 %time (74ms) 80.30% space(26.2MB) 
