class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += "," + str(self.next)
        return string
    
class Stack():
    def __init__(self):
        self.top = None
        self.min = None
    
    def min(self):
        if not self.min:
            return None
        return self.min.value

    def push(self, item):
        if self.min and (self.min < item):
            self.min = Node(value = self.min.value, next = self.min)
        else:
            self.min = Node(value = item, next = self.min)
        self.top = Node(value = item, next = self.top)
    
    def pop(self):
        if not self.top:
            return None
        self.min = self.min.next
        item = self.top.value
        self.top = self.top.next
        return item