from searching import binary_search, agnostic_binary_search

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]

position = binary_search(arr1, -8, 0, len(arr1)-1)
print(position)

arr2 = [101, 98, 57, 49, 13, -3, -17, -61]
position = agnostic_binary_search(arr2, -17)
print(position)
position = agnostic_binary_search(arr2, -61)
print(position)
position = agnostic_binary_search(arr2, 101)
print(position)
position = agnostic_binary_search(arr2, 98)
print(position)
