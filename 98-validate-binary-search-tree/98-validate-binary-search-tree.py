# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root)
        
    
    def valid(self, root, maximum=math.inf, minimum=-math.inf):
        if not root:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
        return self.valid(root.right, maximum, root.val) and self.valid(root.left, root.val, minimum)