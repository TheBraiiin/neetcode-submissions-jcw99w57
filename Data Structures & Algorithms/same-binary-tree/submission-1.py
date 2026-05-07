# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    areSame = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.dfs(p, q)

        return self.areSame

    def dfs(self, p, q):
        if not self.areSame or (not p and not q):
            return

        if not p or not q or (p.val != q.val):
            self.areSame = False
            return 

        self.dfs(p.left, q.left)
        self.dfs(p.right, q.right)

        