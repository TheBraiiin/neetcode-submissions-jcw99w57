# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mheap = []

        self.dfs(root, mheap)

        res = -1

        while mheap and k > 0:
            res = heapq.heappop(mheap)
            k -= 1

        return res

    def dfs(self, root, mheap):
        if not root:
            return

        heapq.heappush(mheap, root.val)

        self.dfs(root.left, mheap)
        self.dfs(root.right, mheap)
