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
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
