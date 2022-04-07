# LINK TO THE PROBLEM = > https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maximum = 0
        for i in root.children:
            value = self.maxDepth(i)
            maximum =  value if maximum < value else maximum
        return maximum + 1
            
        