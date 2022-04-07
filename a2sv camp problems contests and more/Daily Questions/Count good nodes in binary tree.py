LINK TO THE PROBLEM => https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, root.val)
        
    def helper(self, node, maximum):
        if not node:
            return 0
        
        goodNodes = 0
        if node.val >= maximum:
            maximum = node.val
            goodNodes += 1
        
        if node.right:
            goodNodes += self.helper(node.right, maximum)
        if node.left:
            goodNodes += self.helper(node.left, maximum)
        
        return goodNodes
