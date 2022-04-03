# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 

    def helper(self, root, remainSum, lst, res):
      if root.left is None and root.right is None:
          if root.val == remainSum:
              res += [lst + [root.val]]
      if root.left:
          self.helper(root.left, remainSum - root.val, lst + [root.val], res)
      if root.right:
        self.helper(root.right, remainSum - root.val, lst + [root.val], res)
      return res
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
          return []
        return self.helper(root, targetSum, [], [])
      