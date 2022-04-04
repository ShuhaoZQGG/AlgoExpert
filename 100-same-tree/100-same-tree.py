# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversal(root, res = []):
            if root:
                res.append(root.val)
                traversal(root.left, res)
                traversal(root.right, res)
            else:
                res.append(None)
            return res
        
        
        resP = traversal(p, [])
        resQ = traversal(q, [])
        return resP == resQ
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        