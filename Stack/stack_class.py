class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element has been sucessfully inserted"
    
    def pop(self):
        if self.isempty():
            return "There is no element to pop"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.isempty():
            return "There is no element to pop"
        else:
            return self.list[len(self.list)-1]
    
    def delete_entire(self):
        self.list = None