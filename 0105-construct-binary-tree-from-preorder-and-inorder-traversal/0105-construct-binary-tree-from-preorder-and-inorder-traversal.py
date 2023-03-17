# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, inorder, 0, len(inorder) - 1)
    
    def build(self, preorder, index, inorder, start, end):
        if start == end:
            return TreeNode(inorder[start])
        
        if start > end:
            return None
        
        node_index = inorder.index(preorder[index])
        
        node = TreeNode(inorder[node_index])
        node.left = self.build(preorder, index + 1, inorder, start, node_index - 1)
        node.right = self.build(preorder, index + node_index - start + 1, inorder, node_index + 1, end)
        
        return node