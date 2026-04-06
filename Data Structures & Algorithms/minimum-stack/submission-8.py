class MinStack:

    def __init__(self):
        self.topel = 0        
        self.minval = None
        self.stack = list()
    def push(self, val: int) -> None:
        self.stack.insert(self.topel,val)
        self.topel += 1
        if self.minval == None:
            self.minval = val
        elif val < self.minval:
            self.minval = val
    def pop(self) -> None:
        if self.minval == self.top():
            if(self.topel == 1):
                self.minval = None
            else:
                self.minval = min(self.stack[0:self.topel-1])
        self.topel -= 1

    def top(self) -> int:
        return self.stack[self.topel-1]

    def getMin(self) -> int:
        return self.minval
        
