class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node

    def insert(self, value, location):
        if self.head is not None:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            else:
                tempNode = self.head
                i = 0
                while i < location - 1:
                    tempNode = tempNode.next
                    i += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
        else:
            print("The list is empty")
    
    def traverse(self):
        if self.head is not None:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
        else:
            print("The list does not exist")
    
    def reverse_traverse(self):
        if self.head is not None:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
        else:
            print("The list does not exist")
    
    def search(self, value):
        if self.head is not None:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "The value does not exist in the list"
        else:
            return "The list does not exist"
    
    def delete(self, location):
        if self.head is not None:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            else:
                tempNode = self.head
                i = 0
                while i < location - 1:
                    tempNode = tempNode.next
                    i += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
        else:
            print("The list does not exist")

    def deletealll(self):
        if self.head is not None:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        else:
            print("The list does not exits")