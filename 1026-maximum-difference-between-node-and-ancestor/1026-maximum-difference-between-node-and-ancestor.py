# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, node, _max, _min):
        _min = min(_min, node.val)
        _max = max(_max, node.val)
        
        if not node.left and not node.right:
            return abs(_max - _min)
        
        temp_1 = self.dfs(node.right, _max, _min) if node.right else 0
        temp_2  = self.dfs(node.left, _max, _min) if node.left else 0
            
        return max(temp_1, temp_2)
        
            