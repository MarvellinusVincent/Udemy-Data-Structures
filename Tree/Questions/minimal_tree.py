class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    middle = int(len(sortedArray)/2)
    left = minimalTree(sortedArray[:middle])
    right = minimalTree(sortedArray[middle + 1:])
    return BSTNode(sortedArray[middle], left, right)
sortedArray = [1,2,3,4,5,6,7,8,9]
print(minimalTree(sortedArray))