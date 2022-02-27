# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        temp_queue = [(root, 1)]
        ans = 0
        start_y_level = 1 
        
        while queue or temp_queue:
            if not queue:
                _, start_y_level = temp_queue[0]
                queue = deque(temp_queue)
                temp_queue = []
            else:
                node, y_level = queue.popleft()
                ans = max(ans, y_level - start_y_level + 1)
                
                if node.left:
                    temp_queue.append((node.left, y_level * 2))
                if node.right:
                    temp_queue.append((node.right, (y_level * 2) + 1))
        return ans
                