# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()

        self.dfs(root, q)

        res = -1

        while q and k > 0:
            res = q.popleft()
            print(res)
            k -= 1

        return res

    def dfs(self, root, q):
        if not root:
            return

        self.dfs(root.left, q)

        print(root.val)
        q.append(root.val)

        self.dfs(root.right, q)
