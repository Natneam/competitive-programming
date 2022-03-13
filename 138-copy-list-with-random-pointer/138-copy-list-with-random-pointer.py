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
        dummy_node = Node(0)
        mapp = {}
        
        curr_node = dummy_node;
        
        iterator_head = head
        
        while(iterator_head):
            curr_node.next = Node(iterator_head.val)
            
            curr_node = curr_node.next
            
            mapp[iterator_head] = curr_node
            
            iterator_head = iterator_head.next
        
        curr_node = dummy_node.next
        
        while(head):
            if head.random:
                curr_node.random = mapp[head.random]
            curr_node = curr_node.next    
            head = head.next
            
        return dummy_node.next
        
       