import linked_list_queue as queue
class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    
def insert(rootnode, value):
    if rootnode.data == None:
        rootnode.data = value
    elif value < rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild = BST(value)
        else:
            insert(rootnode.leftchild, value)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild = BST(value)
        else:
            insert(rootnode.rightchild, value)
    return "The node has been added"

def preordertraverse(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preordertraverse(rootnode.leftchild)
    preordertraverse(rootnode.rightchild)

def inordertraverse(rootnode):
    if not rootnode:
        return
    inordertraverse(rootnode.leftchild)
    print(rootnode.data)
    inordertraverse(rootnode.rightchild)

def postordertraverse(rootnode):
    if not rootnode:
        return
    postordertraverse(rootnode.leftchild)
    postordertraverse(rootnode.rightchild)
    print(rootnode.data)

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customqueue = queue.Queue
        customqueue.enqueue(rootnode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            print(rootnode.value)
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
    
def search(rootnode, value):
    if rootnode.data == value:
        return True
    elif value < rootnode.data:
        if rootnode.leftchild.data == value:
            return True
        else:
            search(rootnode.leftchild, value)
    else:
        if rootnode.rightchild.data == value:
            return True
        else:
            search(rootnode.rightchild, value)
    return False

def minimumvalue(bstnode):
    current = bstnode
    while (current.leftchild is not None):
        current = current.leftchild
    return current

def delete(rootnode, value):
    if rootnode is None:
        return rootnode
    if value < rootnode.data:
        rootnode.leftchild = delete(rootnode.leftchild, value)
    elif value > rootnode.data:
        rootnode.rightchild = delete(rootnode.rightchild, value)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        if rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = minimumvalue(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = delete(rootnode.rightchild, temp.data)
    return rootnode

def delete_all(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "BST is deleted"
