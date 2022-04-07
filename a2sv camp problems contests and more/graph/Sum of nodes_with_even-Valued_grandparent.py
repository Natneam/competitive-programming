# LINK TO THE PROBLEM => https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        if not root:
            return total
        if root.val % 2 == 0:
            right = root.right
            left = root.left
            if right:
                val = 0
                if right.right:
                    val += right.right.val
                if right.left:
                    val += right.left.val
                total += val 
            if left:
                val = 0
                if left.right:
                    val += left.right.val
                if left.left:
                    val += left.left.val
                total += val
        total += self.sumEvenGrandparent(root.right)
        total += self.sumEvenGrandparent(root.left)
        return total