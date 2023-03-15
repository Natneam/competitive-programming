# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swapped = self.inorder(root)
        original = sorted(swapped[::])
        
        num1 = num2 = None
        
        for i in range(len(swapped)):
            if swapped[i] != original[i]:
                num1 = swapped[i]
                num2 = original[i]
        
        # traverse the tree using dfs and swap num1 and num2
        self.traverse(root, num1, num2)

        
    def traverse(self, node, num1, num2):
        if not node:
            return
        
        if node.val == num1:
            node.val = num2
        elif node.val == num2:
            node.val = num1
            
        self.traverse(node.left, num1, num2)
        self.traverse(node.right, num1, num2)
        
        
    def inorder(self, node):
        res = []
        stack = []
        
        while stack or node:
            if not node:
                res.append(stack[-1].val)
                node = stack.pop().right
            else:
                stack.append(node)
                node = node.left
        return res