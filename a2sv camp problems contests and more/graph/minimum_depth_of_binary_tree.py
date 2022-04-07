# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque()
        if not root:
            return 0
        level = 1
        if self.isLeaf(root):
            return level
        
        queue.append(root)
        
        while len(queue) != 0:
            lengthOfqueue = len(queue)
            for _ in range(lengthOfqueue):
                if not self.isLeaf(queue[0]):
                    if queue[0].left:
                        queue.append(queue[0].left)
                    if queue[0].right:
                        queue.append(queue[0].right)
                    queue.popleft()
                else:
                    return level
            level += 1                
        return level
        
        
    def isLeaf(self, node):
        return not node.right and not node.left