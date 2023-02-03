# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(node, index, level, buff):
            if not node:
                return
            
            if index not in buff:
                buff[index] = [(level, node.val)]
            else:
                buff[index].append((level, node.val))
            
            traverse(node.right, index + 1, level + 1, buff)            
            traverse(node.left, index - 1, level + 1, buff)
        
        buff = {}
        traverse(root, 0, 0, buff)
        
        res = []
        for i in sorted(buff.keys()):
            res.append(map(lambda x : x[1] , sorted(buff[i])))
        
        return res