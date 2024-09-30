#bubble_sort
# def bubble_sort(arr):
#     n = len(arr)
#     for pass_no in range(0, n):
#         for i in range(n-pass_no-1):
#             if arr[i]>arr[i+1]:
#                 arr[i], arr[i + 1] = arr[i+1], arr[i]
#     return arr
# arr = [3,5,6,3,2,6,7]
# print(bubble_sort(arr))

# Selection_sort

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# arr = [1,4,6,7,4,2,1,5,6,96]
# print(selection_sort(arr))

# insertion_sort
def insertion_srot(arr):
    n = len(arr)
    for current in range(1, n):
        currentcard = arr[current]
        currrntpostion = current - 1
        while currrntpostion >= 0:
            if (arr[currrntpostion] < currentcard):
                break
            else:
                arr[currrntpostion + 1] = arr[currrntpostion]
                currrntpostion -= 1
            arr[currrntpostion + 1] = currentcard
    return arr
arr = [3,4,6,3,2,33,4,5]
print(insertion_srot(arr))

