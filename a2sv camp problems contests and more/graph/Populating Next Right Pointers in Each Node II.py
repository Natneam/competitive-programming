# LINK To THE PROBLEM => https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque()
        node1, node2 = None, None
        if root:
            node1 = (root, 0)
            if root.left:
                node2 = (root.left, 1)
                if root.right:
                    queue.append((root.right,1))
                if node2[0].left:
                    queue.append((node2[0].left, 2))
                if node2[0].right:
                    queue.append((node2[0].right, 2))

            elif root.right:
                node2 = (root.right, 1)
                if not node2[0].right and not node2[0].left:
                    return root
                if node2[0].left:
                    queue.append((node2[0].left,2))
                if node2[0].right:
                    queue.append((node2[0].right,2))
            else:
                return root
        else:
            return root

        if node1[1] == node2[1]:
            node1[0].next = node2[0]
            
        while len(queue) != 0:            
            node1 = node2
            node2 = queue.popleft()
            
            if node1[1] == node2[1]:
                node1[0].next = node2[0]
            
            if node2[0].left:
                queue.append((node2[0].left, node2[1]+1))

            if node2[0].right:
                queue.append((node2[0].right, node2[1]+1))
        return root
                