def binary_search_algo(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid + 1
        if arr[mid] > key:
            end = mid - 1
    return -1


arr = [2, 4, 6, 8, 10, 12, 14]
key = 10
result = binary_search_algo(arr, key)

if result == -1:
    print(f"Key not found")
else:
    print(f"key is found at index {result}")
