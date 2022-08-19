def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(low,high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return (i+1)

def quicksort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quicksort(lst, low, pi-1)
        quicksort(lst, pi+1, high)
    return lst
lst = [2,1,7,6,5,9,3,4,8]
print(quicksort(lst, 0, 8))