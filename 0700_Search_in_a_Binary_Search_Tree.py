# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        res = self.levelOrder(root, val)
        return res
      
    def levelOrder(self, root: TreeNode, val):
        q = queue.Queue()
        
        if root:
            q.put(root)
        
        while not q.empty():
            node = q.get()
            if node.val == val:
                return node

            if node.left is not None:
                q.put(node.left)

            if node.right is not None:
                q.put(node.right)
                
        return None

        
