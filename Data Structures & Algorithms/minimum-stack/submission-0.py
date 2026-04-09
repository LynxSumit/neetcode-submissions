class MinStack:

    def __init__(self):
        stack = []
        self.stack = stack

    def push(self, val: int) -> None:
           self.stack.append(val)

    def pop(self) -> None:
           self.stack.pop()

    def top(self) -> int:
          return  self.stack[-1]

    def getMin(self) -> int:
        mini = self.stack[0]
        for el in self.stack:
            mini = min(el, mini)
        return mini
        
