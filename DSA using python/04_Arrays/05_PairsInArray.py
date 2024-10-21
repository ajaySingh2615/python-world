def pairs_in_array(arr):
    tp = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(f"({arr[i]}, {arr[j]})")
            tp += 1
        print("\n")
    print("\n")

    print(f"The total pairs = {tp}")


arr = [2, 4, 6, 8, 10]
pairs_in_array(arr)
