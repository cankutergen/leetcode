# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:        
        # inorder traversel give the descending order
        
        # where we are and kth smallest
        nums = [0] * 2
        
        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)
            
            nums[0] += 1
            if nums[0] == k:
                nums[1] = root.val
                return
                      
            inorder(root.right)
        
        inorder(root)
        return nums[1]
