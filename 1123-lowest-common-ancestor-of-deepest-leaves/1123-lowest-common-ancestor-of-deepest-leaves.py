# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        r, l = self.deepest(root.right), self.deepest(root.left)
        if r == l:
            return root
        elif r > l:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)
    @cache
    def deepest(self, node):
        if not node:
            return 0
        return max(self.deepest(node.right), self.deepest(node.left)) + 1