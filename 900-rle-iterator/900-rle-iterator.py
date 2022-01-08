class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = []
        
        for i in range(0, len(encoding), 2):
            if encoding[i] != 0:
                self.encoding.append(encoding[i])
                self.encoding.append(encoding[i + 1])
        
        self.index = 0
        self.curr_len = self.encoding[0]
        self.curr_val = self.encoding[1]

    def next(self, n: int) -> int:
        if self.index >= len(self.encoding):
            return -1
        
        while n > self.curr_len:
            n -= self.curr_len
            
            self.index += 2
            if self.index < len(self.encoding):
                self.curr_len = self.encoding[self.index]
                self.curr_val = self.encoding[self.index + 1]
            else:
                return -1
        
        if n == self.curr_len:
            val = self.curr_val
            self.index += 2
            if self.index < len(self.encoding):
                self.curr_len = self.encoding[self.index]
                self.curr_val = self.encoding[self.index + 1]                
            return val
        
        self.curr_len -= n
        return self.curr_val
            
        
            
                


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)