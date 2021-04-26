# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(left, right):
            if left > right:
                return None
            
            mid = left + (right - left) // 2
            current = TreeNode(nums[mid])
            current.left = helper(left, mid - 1)
            current.right = helper(mid + 1, right)
            
            return current
            
            
        return helper(0, len(nums) - 1)
