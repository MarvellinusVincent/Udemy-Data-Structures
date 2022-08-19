from inspect import ismemberdescriptor
from matplotlib.contour import ContourLabeler


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " ".join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isempty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isempty():
            return "No node in queue"
        else:
            temp = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head == self.LinkedList.head.next
            return temp
    
    def peek(self):
        if self.isempty():
            return "There is no node in the queue"
        else:
            return self.LinkedList.head
    
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None