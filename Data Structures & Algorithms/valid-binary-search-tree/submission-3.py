# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    isTreeValid = True
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -1001, 1001)

    def isValid(self, root, left, right):
        if not root:
            return True

        if left < root.val < right:
            return self.isValid(root.left, left, root.val) and self.isValid(root.right, root.val, right)
        else:
            return False

           #      5
          #     4   6
        #          3  7