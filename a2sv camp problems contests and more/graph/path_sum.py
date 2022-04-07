# LINK TO THE PROBELM => https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if self.isLeaf(root) and root.val == targetSum:
            return True
        rightCheck = self.hasPathSum(root.right, targetSum-root.val)
        leftCheck = self.hasPathSum(root.left, targetSum-root.val)
        return rightCheck or leftCheck
    
    def isLeaf(self, node):
        if not node.right and not node.left:
            return True
        return False