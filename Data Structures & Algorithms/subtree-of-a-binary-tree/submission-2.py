# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    subtreeMatches = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.dfs(root, subRoot)
        return self.subtreeMatches

    def dfs(self, root, subRoot):
        if not root:
            return

        if self.subtreeMatches:
            return

        if self.compare(root, subRoot):
            self.subtreeMatches = True

        self.dfs(root.left, subRoot)
        self.dfs(root.right, subRoot)


    def compare(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root or not subRoot or root.val != subRoot.val:
            return False

        return self.compare(root.left, subRoot.left) and self.compare(root.right, subRoot.right)