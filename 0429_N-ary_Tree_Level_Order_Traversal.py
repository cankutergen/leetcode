"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        arr = []
        q = queue.Queue()
        
        if root:
            q.put(root)
        
        while not q.empty():
            level = []
            
            for _ in range(q.qsize()):             
                node = q.get()
                level.append(node.val)
                
                for child in node.children:
                    q.put(child)
                    
            arr.append(level)
                
        return arr
