# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    set1 = set()
    curr_head = head1
    while curr_head:
        set1.add(curr_head)
        curr_head = curr_head.next
    curr_head = head2
    while curr_head:
        if curr_head in set1:
            return curr_head.data
        curr_head = curr_head.next

# def findMergeNode(head1, head2):
#  # handling the problem with stack
#     stack1 = list()
#     stack2 = list()
#     curr_head = head1
#     while curr_head:
#         stack1.append(curr_head)
#         curr_head = curr_head.next
#     curr_head = head2
#     while curr_head:
#         stack2.append(curr_head)
#         curr_head = curr_head.next
    
    
#     possible_answer = None
#     while True:
#         try:
#             value_1 = stack1.pop()
#             value_2 = stack2.pop()
#             if value_1 == value_2:
#                 possible_answer = value_1
#             else:
#                 return possible_answer.data
#         except:
#             return possible_answer.data