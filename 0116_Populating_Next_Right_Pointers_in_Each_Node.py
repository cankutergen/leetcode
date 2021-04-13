"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = queue.Queue()
        
        if root:
            root.next = None
            q.put(root)
        else:
            return
            
        while not q.empty():
            
            node = q.get()

            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
            
                q.put(node.left)

                q.put(node.right)
            
        return root
