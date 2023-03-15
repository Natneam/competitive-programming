# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # do bfs and check if the queue at each level is symetric
        queue = deque([root])
        temp_queue = []
        
        while queue or temp_queue:
            if not queue:
                start, end = 0, len(temp_queue) - 1
                
                while start < end:
                    if not temp_queue[start] or not temp_queue[end]:
                        if temp_queue[start] != temp_queue[end]:
                            return False
                    elif temp_queue[start].val != temp_queue[end].val:
                        return False
                    start += 1
                    end -= 1
                    
                queue = deque(temp_queue)
                temp_queue = []
                
            node = queue.popleft()
            
            if not node:
                continue

            temp_queue.append(node.left)
            temp_queue.append(node.right)
        
        return True