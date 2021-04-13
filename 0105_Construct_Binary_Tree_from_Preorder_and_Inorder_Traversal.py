# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder)
        
    def helper(self, preorder, inorder):
        if inorder:
            root = TreeNode(preorder.pop(0))
            mid = inorder.index(root.val)

            arr_len = len(inorder[:mid])
            root.left = self.helper(preorder, inorder[:arr_len])
            root.right = self.helper(preorder, inorder[arr_len + 1:])

            return root
