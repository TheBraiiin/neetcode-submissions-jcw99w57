# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, m):
        if not root:
            return

        m = max(root.val, m)

        if m == root.val:
            self.res += 1
        
        self.dfs(root.left, m)
        self.dfs(root.right, m)