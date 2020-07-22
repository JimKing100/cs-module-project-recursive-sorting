# Merge two sorted array
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    i = 0
    j = 0
    k = 0

    # Traverse the arrays
    while i < len(arrA) and j < len(arrB):
        # If current element is smaller in 1st array, store result and increment
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        # If current element is smaller in 2nd array, store result and increment
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # Store remaining elements if 1st array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    # Store remaining elements of 2nd array
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        L = arr[:middle]
        R = arr[middle:]

        L = merge_sort(L)
        R = merge_sort(R)

        arr = merge(L, R)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input

# Merge two subarrays in merge_in_place
# 1st subarray is arr[start..mid]
# 2nd subarray is arr[mid+1..end]


def merge_in_place(arr, start, mid, end):
    start1 = mid + 1

    # If the direct merge is aready sorted
    if arr[mid] <= arr[start1]:
        return

    # Two pointers (start and start1) to start of subarrays
    while start <= mid and start1 <= end:
        if arr[start] <= arr[start1]:
            start += 1
        else:
            value = arr[start1]
            index = start1

            # Shift elements between element 1 and element 2 right 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Increment pointers
            start += 1
            mid += 1
            start1 += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = (l + r) // 2

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
