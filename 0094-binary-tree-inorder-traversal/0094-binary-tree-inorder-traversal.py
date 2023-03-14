# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = set()
        stack = []
        if root: stack.append(root)
        res = []
        
        while stack:
            if not stack[-1].right and not stack[-1].left:
                res.append(stack[-1].val)
                stack.pop()
            elif stack[-1] not in visited:
                temp = stack[-1]
                if stack[-1].left:
                    stack.append(stack[-1].left)
                visited.add(temp)
            else:
                temp = stack.pop()
                res.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
        return res
                