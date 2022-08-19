def sortedFrequency(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == num:
            left = mid
            right = mid
            while arr[left] == num and left >= 0:
                left -= 1
            while right < len(arr) and arr[right]  == num :
                right += 1
            return right - left - 1
        if arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1