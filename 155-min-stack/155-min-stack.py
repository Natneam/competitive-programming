from sortedcontainers import SortedList

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.getMin()))
        if self.getMin() == None or val < self.getMin():
            self.min = val

    def pop(self) -> None:
        self.min = self.stack.pop()[1]
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()