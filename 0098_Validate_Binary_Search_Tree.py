# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, None, None)
        
    def validate(self, root, max_val, min_val):
        if root is None:
            return True
        elif (max_val is not None and root.val >= max_val) or (min_val is not None and root.val <= min_val): 
            return False
        else:
            return self.validate(root.left, root.val, min_val) and self.validate(root.right, max_val, root.val)
