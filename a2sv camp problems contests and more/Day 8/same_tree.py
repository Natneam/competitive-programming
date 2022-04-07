# LINK TO THE PROBLEM => https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        try:
            self._isSame(p,q)
        except BackToOriginal:
            return False
        return True
    
    def _isSame(self, p, q):
        if not p and not q :
            return
        elif not p or not q:
            raise BackToOriginal
        
        if p.val != q.val:
            raise BackToOriginal
        self._isSame(p.left, q.left)
        self._isSame(p.right, q.right)
    
    
class BackToOriginal(Exception):
        pass