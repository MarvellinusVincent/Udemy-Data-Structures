from inspect import ismemberdescriptor


class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)
    
    def isempty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "The element has been inserted"
    
    def dequeue(self):
        if self.isempty():
            return "There is no element in the list"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isempty():
            return "There is no element in the list"
        else:
            return self.items[0]
    
    def delete(self):
        if self.isempty():
            return "There is no element in the list"
        self.items = None