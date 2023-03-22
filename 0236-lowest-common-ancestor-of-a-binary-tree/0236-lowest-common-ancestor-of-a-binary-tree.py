# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the path to both nodes in the tree
        # from the start of the two paths find latest common node
        _, arr_1 = self.dfs(root, p)
        _, arr_2 = self.dfs(root, q)
        
        arr_1.reverse()
        arr_2.reverse()
        
        res = None
        
        for i in range(min(len(arr_1), len(arr_2))):
            if arr_1[i] == arr_2[i]:
                res = arr_1[i]
        return res
            
        
    def dfs(self, root, node):
        if not root:
            return False, []
        
        if root == node:
            return True, [root]
        
        arr = []
        res_1 = False, []
        res_2 = False, []
        
        if root.right:
            res_1 = self.dfs(root.right, node)
        
        if root.left:
            res_2 = self.dfs(root.left, node)
            
        if res_1[0]:
            res_1[1].append(root)
            arr = res_1[1]
        elif res_2[0]:
            arr = res_2[1].append(root)
            arr = res_2[1]
        else:
            arr = []
        
        return len(arr) > 0, arr
        