# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        remaining = []      
        will_be_deleted = set()
        
        for node in to_delete:
            will_be_deleted.add(node)
            
        def helper(root):
            if root is None:
                return None
            
            root.left = helper(root.left)
            root.right = helper(root.right)
            
            if root.val in will_be_deleted:
                if root.left:
                    remaining.append(root.left)
                    
                if root.right:
                    remaining.append(root.right)
                    
                return None
            
            return root
        
        helper(root)
        if root.val not in will_be_deleted:
            remaining.append(root)
            
        return remaining
