# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def swap(nums):
          x = y = None
          for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
              y = nums[i+1]
              if x is None:
                x = nums[i]
              else:
                break
          return x, y
        
        
        
        def inorderTraversal(root):
          res = []
          stack = []
          while stack or root:
            if root:
              stack.append(root)
              root = root.left
            else:
              root = stack.pop()
              res.append(root.val)
              root = root.right
          return res
        
        def recover(root, x, y, count):
          if root:
            if root.val == x or root.val == y:
              root.val = y if root.val == x else x
              count -= 1
              if count == 0:
                return
            recover(root.left, x, y, count)
            recover(root.right, x, y, count)
            
        nums = inorderTraversal(root)
        x, y = swap(nums)
        recover(root, x, y, 2)