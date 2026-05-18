# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    val = -1
    i = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.val

    def dfs(self, root, k):
        if not root or self.i == k:
            return

        self.dfs(root.left, k)
        self.i += 1
        if self.i == k:
            self.val = root.val
            return
        
        self.dfs(root.right, k)
