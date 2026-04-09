class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        min_num = float('inf')
        for num in self.s:
            min_num = min(min_num, num)
        return min_num

        
