# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isTreeBalanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.subTreeLength(root)

        return self.isTreeBalanced

    def subTreeLength(self, root):
        if not root:
            return 0

        l = self.subTreeLength(root.left)
        r = self.subTreeLength(root.right)

        if l == -1 or r == -1:
            return -1

        if abs(l - r) > 1:
            self.isTreeBalanced = False
            return -1

        return 1 + max(l, r)