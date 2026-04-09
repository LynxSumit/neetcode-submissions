class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))  

    def pop(self) -> None:
        self.minStack.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
