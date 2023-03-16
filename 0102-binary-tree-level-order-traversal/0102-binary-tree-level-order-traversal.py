# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        temp_queue = []
        if root:
            temp_queue.append(root)
            
        res = []
        
        while queue or temp_queue:
            if not queue:
                res.append(list(map(lambda x : x.val, temp_queue)))
                queue = deque(temp_queue)
                temp_queue = []
                
            node = queue.popleft()
            
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        
        return res