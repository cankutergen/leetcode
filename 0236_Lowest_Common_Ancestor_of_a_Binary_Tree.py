# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: 
            return None
        
        p_path = self.pathToNode(root, p, [])
        q_path = self.pathToNode(root, q, [])
        
        if len(p_path) <= len(q_path):
            longer = q_path
            shorter = p_path
        else:
            longer = p_path
            shorter = q_path

        matching = [x for x in longer if x in shorter]
        return matching[-1]
        
    def pathToNode(self, node, x, path):
        if node is None:
            return []
        
        if node.val == x.val:
            path.append(x)
            return path
        
        left = self.pathToNode(node.left, x, path + [node])
        right = self.pathToNode(node.right, x, path + [node])
        
        if left: return left
        if right: return right
        
        
