def print_subarrays_algo(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print("\n")
        print("\n")


arr = [2, 4, 6, 8, 10]
print_subarrays_algo(arr)
