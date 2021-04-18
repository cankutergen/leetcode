class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def huffmanDecode(self, root, arr):
        
        dummy = TreeNode(-1)
        dummy = root
        str = ""
        for i in range(len(arr)):
            if arr[i] == 0:
                dummy = dummy.left
            else:
                dummy = dummy.right

            if dummy and dummy.left is None and dummy.right is None:
                str += dummy.val
                dummy = root

        return str

root = TreeNode("")
dummy1 = TreeNode(".")
dummy2 = TreeNode(".")
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")

root.left = dummy1
root.right = dummy2
dummy1.left = a
dummy1.right = b
dummy2.left = c
dummy2.right = d

sol = Solution()
sol.huffmanDecode(root, [0, 0, 0, 1, 1, 0, 1, 1])
