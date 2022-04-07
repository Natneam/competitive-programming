# LINK TO THE PROBLEM => https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self._helper(root)[1].val
    
    def _helper(self, root):
        if not root.right and not root.left:
            return [1, root]
        val1 = [1, root]
        val2 = [1, root]
        if root.right:
            val1 =  self._helper(root.right)
            val1[0] = val1[0] + 1
        if root.left:
            val2 =  self._helper(root.left)
            val2[0] = val2[0] + 1

        if val1[0] == val2[0]:
            return val2
        else:
            return val2 if val1[0] < val2[0] else val1 
        