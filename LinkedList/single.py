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
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
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
        if self.head is not None:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
        else:
            print("The list does not exist")
    
    def search(self, value):
        if self.head is not None:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
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
        else:
            print("The list does not exits")

test = LinkedList()
test.insert(0,0)
test.insert(2,1)
test.insert(6,1)
print([node.value for node in test])
test.traverse()
test.delete(0)
print([node.value for node in test])