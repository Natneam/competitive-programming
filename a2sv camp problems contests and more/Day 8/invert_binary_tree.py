# LINK TO THE PROBLEM => https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return self._swap(root)
        
    def _swap(self, root):
        if not root:
            return root
        temp = root.right
        root.right = root.left
        root.left = temp
        self.invertTree(root.right)        
        self.invertTree(root.left)
        return root