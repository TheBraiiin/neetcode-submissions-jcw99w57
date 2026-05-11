# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()

        if root:
            q.append((root, 0))

        while q:
            node, i = q.popleft()

            while i > len(res) - 1:
                res.append([])

            res[i].append(node.val)

            if node.left:
                q.append((node.left, i + 1))
            if node.right:
                q.append((node.right, i + 1))
        
        return res
