# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # return self.dfs(root, val)
        return self.bfs(root, val)
        
    def dfs(self, root, val):
        if root is None:
            return None
        
        if root.val == val:
            return root
        elif root.val > val:
            return self.dfs(root.left, val)
        elif root.val < val:
            return self.dfs(root.right, val)

    def bfs(self, root, val):
        q = []
        
        if root:
            q.append(root)
            
        while len(q) > 0:
            node = q.pop(0)
            
            if node.val == val:
                return node
            elif node.val > val and node.left:
                q.append(node.left)
            elif node.val < val and node.right:
                q.append(node.right)
                
        return None

        
