# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        RES = 0
        def preorder(root, SUM):
            nonlocal RES
            if root:
              SUM = SUM*10 + root.val
              if root.left == None and root.right == None:
                RES += SUM
              preorder(root.left, SUM)
              preorder(root.right, SUM)
        preorder(root, 0)
        return RES