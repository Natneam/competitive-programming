"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        queue = deque([node])
        visited = {node.val : Node(node.val)}
        head = visited[node.val]
        
        while queue:
            node = queue.pop()
            curr_node = visited[node.val]
            
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
                    visited[neighbor.val] = Node(neighbor.val)
                
                curr_node.neighbors.append(visited[neighbor.val])
        
        return head
                    