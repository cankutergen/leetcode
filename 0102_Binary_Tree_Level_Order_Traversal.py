# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        arr = []
        q = queue.Queue()
        
        if root:
            q.put(root)
        
        while not q.empty():
            level = []
            
            for _ in range(q.qsize()):             
                node = q.get()
                level.append(node.val)

                if node.left is not None:
                    q.put(node.left)

                if node.right is not None:
                    q.put(node.right)
                    
            arr.append(level)
                
        return arr
