# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:        
        if not root:
          return 0
        if not root.left and not root.right:
          return 1
        
        minDep = float(inf)
        for c in [root.left, root.right]:
            if c:
                minDep = min(self.minDepth(c), minDep)
        
        return minDep + 1
          