# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
    
    def validate(self, root, maximum=math.inf, minimum=-math.inf):
        if not root:
            return True
        
        if root.val >= maximum or root.val <= minimum:
            return False
        
        return self.validate(root.left, root.val, minimum) and self.validate(root.right, maximum, root.val)