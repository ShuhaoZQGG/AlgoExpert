# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        q = collections.deque([(root, root.val)])
        while q:
            node, largest_val = q.popleft()
            if node.left:
                if node.left.val >= largest_val:
                    res += 1
                    q.append((node.left, node.left.val))
                else:
                    q.append((node.left, largest_val))
            if node.right:
                if node.right.val >= largest_val:
                    res += 1
                    q.append((node.right, node.right.val))
                else:
                    q.append((node.right, largest_val))
        return res