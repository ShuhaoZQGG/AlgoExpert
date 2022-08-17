# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, smallest, largest = stack.pop()
            if not node:
                continue
            if node.val <= smallest or node.val >= largest:
                return False
            stack.append((node.left, smallest, node.val))
            stack.append((node.right, node.val, largest))
        return True
        