# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxVal = float("-inf")
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.maxVal
        
    def dfs(self, root):
        if not root:
            return 0

        l = max(self.dfs(root.left), 0)
        r = max(self.dfs(root.right), 0)

        self.maxVal = max(l + r + root.val, self.maxVal)

        return max(l + root.val, r + root.val)