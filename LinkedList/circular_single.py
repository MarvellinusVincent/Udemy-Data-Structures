class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def create(self, value):
        node = Node(value)
        node.next = None
        self.head = node
        self.tail = node
    
    def insert(self, value, location):
        if self.head is None:
            print("The head reference is None")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next == self.head
                self.head = newNode
                self.tail.next = newNode
            else:
                tempNode = self.head
                i = 0
                while i < location - 1:
                    tempNode = tempNode.next
                    i += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def traverse(self):
        if self.head is None:
            print("The head reference is None")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    def search(self, value):
        if self.head is not None:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
                if node == self.tail.next:
                    return "The value does not exist in the list"
        else:
            return "The list does not exist"
    
    def delete(self, location):
        if self.head is not None:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            else:
                tempNode = self.head
                i = 0
                while i < location - 1:
                    tempNode = tempNode.next
                    i += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        else:
            print("The list does not exist")

    def deletealll(self):
        if self.head is not None:
            self.head = None
            self.tail = None
            self.tail.next = None
        else:
            print("The list does not exits")