# LINK TO THE PROBELM => https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._helper(root, -2**(31)-1, (2**(31)))
        
    def _helper(self, root, lowerBound, upperBound):
        if not root:
            return True
        if root.val <= lowerBound or root.val >= upperBound:
            return False
        else:
            val1 = self._helper(root.right, root.val, upperBound)
            val2 = self._helper(root.left, lowerBound, root.val)
            return val1 and val2
#         i = 0
#         j = 1
#         lst = self.inorderTraversal(root, [])
#         while j < len(lst):
#             if lst[i] >= lst[j]:
#                 return False
#             i += 1
#             j += 1
#         return True
    
#     def inorderTraversal(self, root, output):
#         if not root:
#             return None
#         self.inorderTraversal(root.left, output)
#         output.append(root.val)
#         self.inorderTraversal(root.right, output)
#         return output