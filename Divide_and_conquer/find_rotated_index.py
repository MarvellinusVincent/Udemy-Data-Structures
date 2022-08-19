def findRotatedIndex(arr, num):
    left, right = 0, len(arr) - 1
    if len(arr) == 0:
        return -1
    if arr[0] == num:
        return 0
    if arr[-1] == num:
        return arr[-1]
    if arr[left] == arr[right] == arr[int((left + right) / 2)]:
        return -1
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == num:
            return mid
        if arr[mid + 1] < arr[mid]:
            if num >= arr[right]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if num <= arr[left]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

print(findRotatedIndex([3, 4, 1, 2], 4)) # 1
print(findRotatedIndex([4, 6, 7, 8, 9, 1, 2, 3, 4], 8)) # 3
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndex([37, 44, 66, 102, 10, 22], 14)) # -1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
print(findRotatedIndex([11, 12, 13, 14, 15, 16, 3, 5, 7, 9], 16)) # 5
print(findRotatedIndex([11, 12, 13, 17, 39], 17)) # 3
print(findRotatedIndex([11], 11)) # 0
print(findRotatedIndex([], 11)) # -1
print(findRotatedIndex([4, 4, 4, 4, 4], 5)) # -1