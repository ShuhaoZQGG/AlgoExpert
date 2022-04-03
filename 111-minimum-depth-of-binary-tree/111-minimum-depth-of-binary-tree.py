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
        else:
          stack, minDep = [(1, root),], float(inf)
          
        while stack:
          depth, node = stack.pop()
          if not any([node.left, node.right]):
            minDep = min(depth, minDep)
            
          for c in [node.left, node.right]:
            if c:
              stack.append((depth + 1, c))
          
        
        return minDep
          