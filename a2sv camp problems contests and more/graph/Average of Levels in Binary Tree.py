# LINK TO THE PROBLEM => https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        result = []
        level = 0
        summation = 0
        number = 0
        
        queue.append((root,0))

        while queue:
            currNode = queue.popleft()
            if level == currNode[1]:
                summation += currNode[0].val
                number += 1
                
            if level + 1 == currNode[1]:
                result.append(float("{:.5f}".format(summation/number)))
                
                level += 1
                number = 1
                summation = currNode[0].val
            if currNode[0].right:
                queue.append((currNode[0].right, currNode[1]+1))
            if currNode[0].left:
                queue.append((currNode[0].left, currNode[1]+1))
        result.append(float("{:.5f}".format(summation/number)))
        return result
            