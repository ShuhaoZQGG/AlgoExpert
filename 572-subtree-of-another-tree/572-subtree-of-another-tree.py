# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return isSame(root.left, subRoot.left) and isSame(root.right, subRoot.right)
        
        q = collections.deque([(root, subRoot)])
        while q:
            root, subRoot = q.popleft()
            if isSame(root, subRoot):
                return True
            if not isSame(root,subRoot):
                if root:
                    q.append((root.left, subRoot))
                    q.append((root.right, subRoot))
        return False
            