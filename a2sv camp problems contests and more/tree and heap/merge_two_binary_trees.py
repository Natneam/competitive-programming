# LINK TO THE PROBLEM => https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self._merge(t1,t2)
    
    def _merge(self, t1, t2):
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2 != None:
            node = TreeNode(t2.val+0)
            node.left = self._merge(None, t2.left)
            node.right = self._merge(None, t2.right)
            return node
        elif t2 == None and t1 != None:
            node = TreeNode(t1.val+0)
            node.left = self._merge(t1.left, None)
            node.right = self._merge(t1.right,None)
            return node
        else:
            node = TreeNode(t1.val+t2.val)
            node.left = self._merge(t1.left,t2.left)
            node.right = self._merge(t1.right,t2.right)
            return node
            