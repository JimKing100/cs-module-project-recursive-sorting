def binary_search(arr, target, start, end):
    if end >= start:
        middle = (start + end) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)
        else:
            return binary_search(arr, target, middle + 1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    if len(arr) > 1:
        if arr[0] < arr[1]:
            ascending = True
        else:
            ascending = False
    else:
        ascending = True

    if ascending is True:
        position = binary_search(arr, target, 0, len(arr) - 1)
        return position
    else:
        position = binary_search(sorted(arr), target, 0, len(arr) - 1)
        if position == -1:
            return -1
        else:
            return len(arr) - position - 1
