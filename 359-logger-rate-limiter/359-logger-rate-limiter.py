class Logger:

    def __init__(self):
        self.message_stamp = {}  #message => last_valid_stamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_stamp:
            self.message_stamp[message] = timestamp
            return True
        elif timestamp - self.message_stamp[message] >= 10:
            self.message_stamp[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)