from logging import root
from tkinter.tix import Tree
from Udemy.Tree.binary_search_tree import insert
import linked_list_queue as queue

class TreeAVL:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
    
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

def getheight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightrotate_LL(disbalancednode):
    newroot = disbalancednode.leftchild
    disbalancednode.leftchild = disbalancednode.leftchild.rightchild
    newroot.rightchild = disbalancednode
    disbalancednode.height = 1 + max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

def leftrotate_RR(disbalancednode):
    newroot = disbalancednode.rightchild
    disbalancednode.rightchild = disbalancednode.rightchild.leftchild
    newroot.leftchild = disbalancednode
    disbalancednode.height = 1 + max(getheight(disbalancednode.leftchild), getheight(disbalancednode.rightchild))
    newroot.height = 1 + max(getheight(newroot.leftchild), getheight(newroot.rightchild))
    return newroot

def getbalanced(rootnode):
    if not rootnode:
        return 0
    return getheight(rootnode.leftchild) - getheight(rootnode.rightchild)

def insertnode(rootnode, value):
    if not rootnode:
        return TreeAVL(value)
    elif value < rootnode.data:
        rootnode.leftchild = insertnode(rootnode.leftchild, value)
    else:
        rootnode.rightchild = insertnode(rootnode.rightchild, value)
    rootnode.height = 1 + max(getheight(rootnode.leftchild), getheight(rootnode.rightchild))
    balanced = getbalanced(rootnode)
    if balanced > 1 and value < rootnode.leftchild.data:
        return rightrotate_LL(rootnode)
    if balanced > 1 and value < rootnode.leftchild.data:
        rootnode.leftchild = leftrotate_RR(rootnode.leftchild)
        return rightrotate_LL(rootnode)
    if balanced < -1 and value > rootnode.rightchild.data:
        return leftrotate_RR(rootnode)
    if balanced > 1 and value < rootnode.rightchild.data:
        rootnode.rightchild = rightrotate_LL(rootnode.rightchild)
        return leftrotate_RR(rootnode)

def getminvaluenode(rootnode):
    if rootnode is None or rootnode.leftchild is None:
        return rootnode
    return getminvaluenode(rootnode.leftchild)

def delete(rootnode, value):
    if not rootnode:
        return rootnode
    elif value < rootnode.data:
        rootnode.leftchild = delete(rootnode.leftchild, value)
    elif value > rootnode.data:
        rootnode.rightchild = delete(rootnode.rightchild, value)
    else:
        if rootnode.leftchild is None:
            temp = rootnode.rightchild
            rootnode = None
            return temp
        elif rootnode.rightchild is None:
            temp = rootnode.leftchild
            rootnode = None
            return temp
        temp = getminvaluenode(rootnode.rightchild)
        rootnode.data = temp.data
        rootnode.rightchild = delete(rootnode.rightchild, temp.data)
    balanced = getbalanced(rootnode)
    if balanced > 1 and getbalanced(rootnode.leftchild) >= 0:
        return rightrotate_LL(rootnode)
    if balanced < -1 and getbalanced(rootnode.rightchild) <= 0:
        return leftrotate_RR(rootnode)
    if balanced > 1 and getbalanced(rootnode.leftchild) < 0:
        rootnode.leftchild = leftrotate_RR(rootnode.leftchild)
        return rightrotate_LL(rootnode)
    if balanced < 1 and getbalanced(rootnode.rightchild) > 0:
        rootnode.rightchild = rightrotate_LL(rootnode.rightchild)
        return leftrotate_RR(rootnode)

def delete_all(rootnode):
    rootnode = None
    rootnode.leftchild = None
    rootnode.rightchild = None
    return "The tree has been deleted"