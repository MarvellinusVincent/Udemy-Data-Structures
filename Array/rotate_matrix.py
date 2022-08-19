import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def rotatearray(arr):
    n = len(arr)
    for num_rotation in range(n//2):
        first = num_rotation
        last = n - num_rotation - 1
        for each_rotation in range(first, last):
            top = arr[num_rotation][each_rotation]
            arr[num_rotation][each_rotation] = arr[-each_rotation-1][num_rotation]
            arr[-each_rotation-1][num_rotation] = arr[-num_rotation-1][-each_rotation-1]
            arr[-num_rotation-1][-each_rotation-1] = arr[each_rotation][-num_rotation-1]
            arr[each_rotation][-num_rotation-1] = top
    return arr
