# LINK TO THE PROBLEM -> https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None        

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def get(self, index: int, ret=0) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        current = self.head
        counter = 0
        while current != None:
            if counter == index:
                if ret == 0:
                    return current.val
                else:
                    return current
            counter += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head
        prev = None
        while current != None:
            prev = current
            current = current.next
        if prev == None:
            self.head = Node(val)
        else:
            prev.next = Node(val) 
        
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            temp = self.head
            self.head = Node(val)
            self.head.next = None
        else:
            current = self.get(index,ret=1)
            if current != -1:
                prev = self.get(index-1,ret=1)
                prev.next = Node(val)
                prev.next.next = current
            elif len(self) == index:
                self.addAtTail(val)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        current = self.get(index, ret=1)
        if current == self.head:
            current = self.head
            self.head = self.head.next
            return 
        if current != -1:
            prev = self.get(index-1, ret=1)
            prev.next = current.next
        
    def __len__(self):
        '''return the length of the linked list'''
        length  = 0
        current = self.head
        while current != None:
            length += 1
            current = current.next
        return length

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)