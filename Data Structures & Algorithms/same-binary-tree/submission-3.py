# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pd = deque()
        qd = deque()
        
        pd.append(p)
        qd.append(q)

        while pd and qd:
            pnode = pd.popleft()
            qnode = qd.popleft()

            if not pnode and not qnode:
                continue

            if not pnode or not qnode:
                return False

            if pnode.val != qnode.val:
                return False

            pd.append(pnode.left)
            pd.append(pnode.right)
            qd.append(qnode.left)
            qd.append(qnode.right)

        return len(pd) == len(qd)