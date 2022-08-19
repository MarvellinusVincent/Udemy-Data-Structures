import math
def binary(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start+end)/2)
    for i in range(len(array)//2):
        if value < array[middle]:
            end = middle
        elif value > array[middle]:
            start = middle
        else:
            return middle
        middle = math.floor((start+end)/2)
    return -1