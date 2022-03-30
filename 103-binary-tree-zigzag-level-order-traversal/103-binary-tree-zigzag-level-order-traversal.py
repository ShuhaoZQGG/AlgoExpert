# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []
      level_list = deque()
      if root is None:
        return []
      node_queue = deque([root, None])
      left_to_right = True
      
      while node_queue:
        curr_node = node_queue.popleft()
        
        if curr_node:
          if left_to_right:
            level_list.append(curr_node.val)
          else:
            level_list.appendleft(curr_node.val)
            
          if curr_node.left:
            node_queue.append(curr_node.left)
            
          if curr_node.right:
            node_queue.append(curr_node.right)
          
        else:
          res.append(level_list)
          if node_queue:
            node_queue.append(None)
          level_list = deque()
          left_to_right = not left_to_right
      return res