# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isTreeValid = True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root, -1001, 1001)
    
        return self.isTreeValid

    def dfs(self, root, low, high):
        if not root or not self.isTreeValid:
            return 

        if root.val <= low or root.val >= high:
            self.isTreeValid = False

        if (root.left and root.left.val >= root.val 
            or root.right and root.right.val <= root.val):
            self.isTreeValid = False

        self.dfs(root.left, low, min(high, root.val))
        self.dfs(root.right, max(low, root.val), high)


           #      5
          #     4   6
        #          3  7