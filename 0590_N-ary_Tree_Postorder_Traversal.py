"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        res = self.traverse(root, arr)
        return arr
        
    def traverse(self, root, arr):
        if root:
            for child in root.children:
                self.traverse(child, arr)
                
            arr.append(root.val)
        
