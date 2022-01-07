class Node:
    def __init__(self, key=None, val =None,  prev=None, _next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = _next
        
    # def __repr__(self):
    #     return f"[{self.key} | {self.prev.val} | {self.next.val}] "
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node()
        self.tail = Node(None, None, self.head, None)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        value = self.delete(key)
        self.put(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.delete(key)
            self.put(key, value)
            return
        
        if self.capacity == 0:
            self.delete(self.tail.prev.key)
            self.put(key, value)
            return
        
        temp = self.head.next
        self.head.next = Node(key, value, self.head, self.head.next)
        temp.prev = self.head.next
        
        self.hash_map[key] = self.head.next
        self.capacity -= 1
    
    def delete(self, key):
        self.capacity += 1
        node = self.hash_map[key]
        
        val = node.val
        
        _next = node.next
        _prev = node.prev
        
        _prev.next = _next
        _next.prev = _prev
        
        del self.hash_map[key]
        return val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Use dobly linked list with hashtable(dictonary)
"""