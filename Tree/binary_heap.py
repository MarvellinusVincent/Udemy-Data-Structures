from heapq import heapify


class BinaryHeap:
    def __init__(self, size):
        self.customlist = (size + 1) * [None]
        self.heapsize = 0
        self.maxsize = size + 1
    
def peak(rootnode):
    if not rootnode:
        return
    return rootnode.customlist[1]

def size(rootnode):
    if not rootnode:
        return
    return rootnode.heapsize

def level_order_traverse(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1, rootnode.heapsize + 1):
            print(rootnode.customlist[i])

def heapifytreeinsert(rootnode, index, heaptype):
    parentindex = int(index / 2)
    if index <= 1:
        return
    if heaptype == "Min":
        if rootnode.customlist[index] < rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapifytreeinsert(rootnode, parentindex, heaptype)
    elif heaptype == "Max":
        if rootnode.customlist[index] > rootnode.customlist[parentindex]:
            temp = rootnode.customlist[index]
            rootnode.customlist[index] = rootnode.customlist[parentindex]
            rootnode.customlist[parentindex] = temp
        heapifytreeinsert(rootnode, parentindex, heaptype)

def insert(rootnode, value, heaptype):
    if rootnode.heapsize + 1 == rootnode.maxsize:
        return "The binary heap is full"
    rootnode.customlist[rootnode.heapsize + 1] = value
    rootnode.heapsize += 1
    heapifytreeinsert(rootnode, rootnode.heapsize, heaptype)
    return "The heap has been inserted"

def heapifytreeextract(rootnode, index, heaptype):
    leftindex = index * 2
    rightindex = index * 2 + 1
    swapchild = 0
    if rootnode.heapsize < leftindex:
        return
    elif rootnode.heapsize == leftindex:
        if heaptype == "Min":
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
        else:
            if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
            return
    else:
        if heaptype == "Min":
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[index] > rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
        else:
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                swapchild = leftindex
            else:
                swapchild = rightindex
            if rootnode.customlist[index] < rootnode.customlist[swapchild]:
                temp = rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[swapchild]
                rootnode.customlist[swapchild] = temp
    heapifytreeextract(rootnode, swapchild, heaptype)

def extract(rootnode, heaptype):
    if rootnode.heapsize == 0:
        return
    else:
        extractednode = rootnode.customlist[1]
        rootnode.customlist[1] = rootnode.customlist[rootnode.heapsize]
        rootnode.customlist[rootnode.heapsize] = None
        rootnode.heapsize -= 1
        heapifytreeextract(rootnode, 1, heaptype)
        return extractednode

def delete(rootnode):
    rootnode.customlist = None