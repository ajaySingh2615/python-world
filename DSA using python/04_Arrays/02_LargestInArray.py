def largest_algo(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = [1, 2, 6, 3, 5]
result = largest_algo(arr)
print(f"The largest element is: {result}")
