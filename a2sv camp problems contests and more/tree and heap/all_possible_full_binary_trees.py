# LINK TO THE PROBLEM => https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N%2 == 0:
            return None
        if N == 1:
            return [TreeNode()]
        arr = []
        for i in range(1,N,2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-i-1)
            for nodeR in right:
                for nodeL in left:
                    mainNode = TreeNode()
                    mainNode.right = nodeR
                    mainNode.left = nodeL
                    arr.append(mainNode)
        return arr