# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_node = ListNode()
        heap = [[lists[i].val, i, lists[i]] for i in range(len(lists)) if lists[i]]
        heapq.heapify(heap)
        curr_node = dummy_node
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr_node.next = node
            curr_node = curr_node.next
            
            if node.next:
                heapq.heappush(heap, [node.next.val, i, node.next])
        
        return dummy_node.next
        