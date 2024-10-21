def reverse_an_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


arr = [2, 4, 6, 8, 10]
reverse_an_array(arr)
print(arr)
