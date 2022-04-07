# LINK TO THE PROBLEM => https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = list()
        self.stack2 = list()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        output = self.stack1.pop()
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        return output
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
        output = self.stack1[0]
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())
        return output
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if len(self.stack1) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()