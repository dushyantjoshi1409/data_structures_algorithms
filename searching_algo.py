def binart_search(arr, target):
    start_index = 0
    last_index = len(arr)-1
    while start_index <= last_index:
        mid = (start_index+last_index)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            last_index = mid - 1
        elif arr[mid] < target:
            start_index = mid + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7]
target = 1
print(binart_search(arr, target))
