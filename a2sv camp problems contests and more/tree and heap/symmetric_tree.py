# LINK TO THE PROBLEM => https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._inorder(root.right, root.left)
    
    def _inorder(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2:
            if tree1.val != tree2.val:
                return False
            val1 = self._inorder(tree1.right, tree2.left)
            val2 = self._inorder(tree1.left, tree2.right)
            return val1 and val2
        return False