# LINK TO THE PROBLEM => https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = deque()
        level = 0
        result = []
        
        if root:
            queue.append((root,0))
        
        while queue:
            currNode = queue.popleft()
            if level == currNode[1]:
                result.append(currNode[0].val)
                level += 1
            
            if currNode[0].right != None:
                queue.append((currNode[0].right, currNode[1]+1))
            if currNode[0].left != None:
                queue.append((currNode[0].left, currNode[1]+1))
        return result