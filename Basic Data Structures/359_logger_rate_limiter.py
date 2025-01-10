class Logger:

    def __init__(self):
        """
        O(1) for shouldPrintMessage
        O(nm) n num of unique messages, m is the ave length of a message  
        """
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamp or timestamp >= self.message_timestamp[message]:
            # Update the next allowed timestamp for the message
            self.message_timestamp[message] = timestamp + 10
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)