def linear_search_algo(li, key):
    for i in range(len(li)):
        if li[i] == key:
            return i + 1

    return -1


li = [2, 4, 6, 8, 10, 12, 14, 16]
key = 10

result = linear_search_algo(li, key)

if result == -1:
    print(f"Key is not found")
else:
    print(f"{key} is found at index {result}")
