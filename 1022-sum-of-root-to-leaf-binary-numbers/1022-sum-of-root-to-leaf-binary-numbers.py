# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def root_to_leaf(root):
            if not root.right and not root.left:
                return [[str(root.val)]]
            
            paths = []
            if root.right:
                for item in root_to_leaf(root.right):
                    paths.append(item)
                
            if root.left:
                for item in root_to_leaf(root.left):
                    paths.append(item)
            
            for i in range(len(paths)):
                paths[i].append(str(root.val))
            
            return paths
        ans = 0
        
        for string in root_to_leaf(root):
            ans += int("".join(reversed(string)), 2)
        
        return ans