# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxLen = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getLength(root)

        return self.maxLen

    def getLength(self, root):
        if not root:
            return 0

        l = self.getLength(root.left)
        r = self.getLength(root.right)

        self.maxLen = max(self.maxLen, l + r)

        return 1 + max(l, r)