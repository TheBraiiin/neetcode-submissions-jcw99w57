# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isTreeValid = True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root, float("-inf"), float("inf"))
        return self.isTreeValid

    def dfs(self, root, l, r):
        if not root:
            return

        if l < root.val < r:
            self.dfs(root.left, l, root.val)
            self.dfs(root.right, root.val, r)
        else:
            self.isTreeValid = False
