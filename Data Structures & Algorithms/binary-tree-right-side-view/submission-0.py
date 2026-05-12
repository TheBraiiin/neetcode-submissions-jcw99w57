# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dq = deque()

        if root:
            dq.append((root, 0))

        while dq:
            node, lvl = dq.popleft()
            print(node.val)
            if len(res) < lvl + 1:
                res.append(node.val)
            
            if node.right:
                dq.append((node.right, lvl + 1))
            if node.left:
                dq.append((node.left, lvl + 1))

        return res