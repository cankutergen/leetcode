# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr = []
        self.traverse(root, arr)
        return arr
    
    def traverse(self, root, arr):
        if root:
            self.traverse(root.left, arr)
            arr.append(root.val)
            self.traverse(root.right, arr)
