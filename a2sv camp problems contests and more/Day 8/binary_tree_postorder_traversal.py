# LINK TO THE PROBLEM => https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output_list = []
        self._traverse(root, output_list)
        return output_list
    
    def _traverse(self, root, output_list):
        if not root:
            return
        self._traverse(root.left, output_list)
        self._traverse(root.right, output_list)
        output_list.append(root.val)