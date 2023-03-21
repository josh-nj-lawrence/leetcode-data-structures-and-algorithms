# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currmax):
            if not node:
                return 0
            left = dfs(node.left, max(currmax, node.val))
            right = dfs(node.right, max(currmax, node.val))
            ans = left + right
            if node.val >= currmax:
                ans += 1
            return ans
        
        return dfs(root, float("-inf"))

# Results: 31.52% time (283ms) 79.60% space (32.5MB)