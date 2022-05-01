# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0
        res = []
        q = collections.deque([root])
        while q:
            res.append([])
            for i in range(len(q)):
                root = q.popleft()
                res[level].append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            level += 1
        return res