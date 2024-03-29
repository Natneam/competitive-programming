# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
    
    def helper(self, node):
        if not node:
            return 0, 0
        left, right = self.helper(node.left), self.helper(node.right)
        return left[0] + right[0] + node.val, abs(left[0] - right[0]) + right[1] + left[1]