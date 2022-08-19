from distutils.sysconfig import customize_compiler
import linked_list_queue as queue

class BinaryTreeLL:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    
def preorder_traverse(rootnode):
    if not rootnode:
        return
    print(rootnode.data)

def inorder_traverse(rootnode):
    if not rootnode:
        return
    inorder_traverse(rootnode.leftchild)
    print(rootnode.data)
    inorder_traverse(rootnode.rightchild)
    print(rootnode.data)

def postoder_traverse(rootnode):
    if not rootnode:
        return
    postoder_traverse(rootnode.leftchild)
    postoder_traverse(rootnode.rightchild)
    print(rootnode.data)

def levelorder_traverse(rootnode):
    if not rootnode:
        return
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.leftchild)
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.rightchild)

def search(rootnode, nodevalue):
    if not rootnode:
        return "The Binary Tree does not exist"
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.data == nodevalue:
                return "Success"
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.leftchild)
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.rightchild)
        return "Not found"

def insert(rootnode, newnode):
    if not rootnode:
        rootnode = newnode
    else:
        customqueue = queue.Queue()
        customqueue.dequeue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild = newnode
                return "Successful"
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newnode
                return "Successful"
                
def delete(rootnode):
    if not rootnode:
        return 
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.leftchild)
            if (root.value.leftchild) is not None:
                customqueue.enqueue(root.value.rightchild)
        deepestnode = root.value
        return deepestnode

def delete_all(rootnode):
    rootnode.data = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "Successful"