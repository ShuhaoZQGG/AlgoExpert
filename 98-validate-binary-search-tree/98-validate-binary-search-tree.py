# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def validate(root, smallest=-math.inf, largest = math.inf):
            if root is None:
                return True
            if root.val <= smallest or root.val >= largest:
                return False
            return validate(root.left, smallest, root.val) and validate(root.right, root.val, largest)
        
        return validate(root)