class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_idx = []

    def push(self, val):
        self.stack.append(val)
        if len(self.min_idx) == 0:
            self.min_idx.append(0)
        elif self.stack[self.min_idx[-1]] > val:
            self.min_idx.append(len(self.stack)-1)

    def pop(self):
        if self.min_idx[-1] == len(self.stack) - 1:
            self.min_idx.pop()
        self.stack.pop() 

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.stack[self.min_idx[-1]]
        