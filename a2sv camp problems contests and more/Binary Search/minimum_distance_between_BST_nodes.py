# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        sortedList = self._inorder(root, [])
        minDiff = 2**32
        for i in range(len(sortedList)-1):
            diff = sortedList[i] - sortedList[i+1]
            if diff  < minDiff:
                minDiff = diff
        return minDiff
                
        
    def _inorder(self, root, output):
        if not root:
            return
        self._inorder(root.right, output)
        output.append(root.val)
        self._inorder(root.left, output)
        return output