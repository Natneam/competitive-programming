#LINK TO THE PROBLEM => https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        paths = sorted(self.dfs(root, []),key= lambda a: -len(a))
        
        deepestNodes = []
        maxDepth = len(paths[0])
        for item in paths:
            if len(item) == maxDepth:
                deepestNodes.append(item)
                
        if len(deepestNodes) == 1:
            return deepestNodes[0][-1]
        
        for pos in range(len(deepestNodes[0])):
            val = deepestNodes[0][pos]
            for item in deepestNodes:
                if item[pos] != val:
                    return item[pos-1]
                  
    def dfs(self, node, prevNodes):
        if not node.right and not node.left:
            prevNodes.append(node)
            return [prevNodes]
        path  = []
        if node.right:
            path += self.dfs(node.right, [x for x in prevNodes] + [node])
        if node.left:
            path += self.dfs(node.left, [x for x in prevNodes] + [node])
        return path
