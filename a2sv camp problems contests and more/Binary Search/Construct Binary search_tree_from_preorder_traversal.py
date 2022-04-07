# LINK TO THE PROBLEM => https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # return self._helper(preorder, 0, len(preorder)-1)
        if len(preorder) == 0:
            return None      
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        nodeVal = preorder[0]
        node = TreeNode(nodeVal)
        index = None
        for i,v in enumerate(preorder):
            if v > nodeVal:
                index = i
                break
        if index == None:
            node.left = self.bstFromPreorder(preorder[1:])
            node.right = None
            return node

        node.left = self.bstFromPreorder(preorder[1:index])
        node.right = self.bstFromPreorder(preorder[index:])

        return node

#     using indices rather than slicing
#     def _helper(self, preorder, start, end):
#         if start > end:
#             return None      
#         if start == end:
#             return TreeNode(preorder[start])
#         nodeVal = preorder[start]
#         node = TreeNode(nodeVal)
#         index = None
#         for i in range(start,end+1):
#             if preorder[i] > nodeVal:
#                 index = i
#                 break
#         if index == None:
#             node.left = self._helper(preorder, start+1, end)
#             node.right = None
#             return node
#         node.left = self._helper(preorder, start+1, index-1)
#         node.right = self._helper(preorder, index, end)
        
#         return node