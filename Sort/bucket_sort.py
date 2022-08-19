import math
import insertion_sort as insertionsort
def bucketsort(lst):
    numberofBuckets = round(math.sqrt(len(lst)))
    maxValue = max(lst)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in lst:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertionsort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            lst[k] = arr[i][j]
            k += 1
    return lst
lst = [2,1,7,6,5,9,3,4,8]
print(bucketsort(lst))