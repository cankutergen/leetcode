"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        self.traverse(root, arr)
        return arr
        
    def traverse(self, root, arr):
        
        if root:
            arr.append(root.val)
            
            for child in root.children:
                self.traverse(child, arr)
