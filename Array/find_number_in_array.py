import numpy as np

array = np.array([1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15])

def find_number(arr, num):
    for number in range(len(array)):
        if arr[number] == num:
            print(number)
