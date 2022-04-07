# LINK TO THE PROBLEM => https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        digits = self.dfs(root, [])
        stringDigits = []
        for item in digits:
            stringDigits.append([str(i) for i in item])
        return sum([int(''.join(x)) for x in stringDigits])
        
    def dfs(self, node, prevNodes):
        if not node.right and not node.left:
            prevNodes.append(node.val)
            return [prevNodes]
        digits  = []
        if node.right:
            digits += self.dfs(node.right, [x for x in prevNodes] + [node.val])
        if node.left:
            digits += self.dfs(node.left, [x for x in prevNodes] + [node.val])
        return digits