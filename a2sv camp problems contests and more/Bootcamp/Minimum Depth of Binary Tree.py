# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append([root,1])
        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.right and not node.left:
                    return depth
                try:
                    queue.append([node.right, depth + 1])
                except:
                    pass
                try:
                    queue.append([node.left, depth + 1])
                except:
                    pass