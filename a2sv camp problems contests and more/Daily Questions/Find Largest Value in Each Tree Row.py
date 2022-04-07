# LINK TO THE PROBLEM => https://leetcode.com/problems/find-largest-value-in-each-tree-row/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        output = [-float('inf')]
        currRow = 0
        
        queue.append((root, 0))
        
        while queue:
            currElement = queue.popleft()
            
            if currElement[1] == currRow:
                output[currRow] = max(output[currRow], currElement[0].val)
            else:
                currRow = currElement[1]
                output.append(currElement[0].val)
                
            
            if currElement[0].left:
                queue.append((currElement[0].left, currElement[1] + 1))
            
            if currElement[0].right:
                queue.append((currElement[0].right, currElement[1] + 1))
        
        return output
                
