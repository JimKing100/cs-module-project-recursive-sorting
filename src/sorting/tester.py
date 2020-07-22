from sorting import merge, merge_sort, merge_sort_in_place

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

result = merge(arr1, arr2)
print(result)

arr3 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
result = merge_sort(arr3)
print(result)

merge_sort_in_place(arr3, 0, len(arr3) - 1)
print(arr3)
