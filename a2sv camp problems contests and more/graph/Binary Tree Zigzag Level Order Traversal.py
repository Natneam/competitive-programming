# LINK TO THE PROBLEM => https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        level = 0
        direction = -1
        currLevelNodes = []
        result = []
        
        if root:
            queue.append((root, 0))
                
        while queue:
            currNode = queue.popleft()
            
            if level == currNode[1]:
                currLevelNodes.append(currNode[0].val)
            elif level + 1 == currNode[1]:
                if direction == 1:
                    result.append(reversed(currLevelNodes))
                else:
                    result.append(currLevelNodes)
                currLevelNodes = [currNode[0].val]
                level += 1
                direction *= -1
            
            if currNode[0].left:
                queue.append((currNode[0].left, currNode[1] + 1))
            if currNode[0].right:
                queue.append((currNode[0].right, currNode[1] + 1))

        if currLevelNodes: 
            if direction == 1:
                result.append(reversed(currLevelNodes))
            else:
                result.append(currLevelNodes)
        return result
                
            