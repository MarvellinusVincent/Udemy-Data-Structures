class BinaryTreeL:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastusedindex = 0
        self.maxsize = size
    
    def insertnode(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "The Binary Tree is full"
        self.customlist[self.lastusedindex + 1] = value
        self.lastusedindex += 1
        return "The value has been successfully added"
    
    def search(self, nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i] == nodevalue:
                return True
            return False
    
    def preordertraverse(self, index):
        if index > self.lastusedindex:
            return
        print(self.customlist[index])
        self.preordertraverse(index * 2)
        self.preordertraverse(index * 2 + 1)
    
    def inordertraverse(self, index):
        if index > self.lastusedindex:
            return
        self.inordertraverse(index * 2)
        print(self.customlist[index])
        self.inordertraverse(index * 2 + 1)
    
    def postordertraverse(self, index):
        if index > self.lastusedindex:
            return
        self.postordertraverse(index * 2)
        self.postordertraverse(index * 2 + 1)
        print(self.customlist[index])
    
    def levelordertraverse(self, index):
        for i in range(index, self.lastusedindex + 1):
            print(self.customlist[i])

    def delete(self, value):
        if self.lastusedindex == 0:
            return "There is no node to delete"
        for i in range(1, self.lastusedindex + 1):
            if self.customlist[i] == value:
                self.customlist[i] = self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex] = None
                self.lastusedindex -= 1
                return "The node has been deleted"
    
    def delete_all(self):
        self.customlist = None
        return "The Binary Tree has been deleted"