# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        
        self.dfs(root, val)
        return root
        
    def dfs(self, root, val):       
        if root is None:
            return
        
        if root.left is None and root.val > val:
            root.left = TreeNode(val)
        elif root.right is None and root.val < val:
            root.right = TreeNode(val)
          
        if root.val > val:
            self.dfs(root.left, val)
        elif root.val < val:
            self.dfs(root.right, val)
