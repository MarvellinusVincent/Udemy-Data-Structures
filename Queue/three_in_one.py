from inspect import stack
from tokenize import Triple


class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
    
    def isfull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        return False
    
    def isempty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        return False
    
    def indexoftop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset * self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isfull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexoftop(stacknum)] == item
    
    def pop(self, stacknum):
        if self.isempty(stacknum):
            return "The stack isempty"
        else:
            value = self.custList[self.indexoftop(stacknum)]
            self.custList[self.indexoftop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.isempty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexoftop(stacknum)]
            return value
