# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        
        def findPaths(root, total, current, paths):
            if root is None:
                return 
            
            current.append(root.val)
            if root.val == total and root.left is None and root.right is None:
                paths.append(current)
                return    
            
            findPaths(root.left, total - root.val, current.copy(), paths)
            findPaths(root.right, total - root.val, current.copy(), paths)
        
        findPaths(root, targetSum, [], paths)
        return paths
