"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping, dummy = dict(), Node(0)
        
        curr, copy = head, dummy
        while curr:
            copy.next = Node(curr.val)
            mapping[curr] = copy.next
            curr, copy = curr.next, copy.next
            
        curr, copy = head, dummy.next
        while curr:
            copy.random = mapping[curr.random] if curr.random else None
            curr, copy = curr.next, copy.next
                
        return dummy.next