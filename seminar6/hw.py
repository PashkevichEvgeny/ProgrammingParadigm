def binary_search(target, array, i=0):
    half = len(array) // 2
    if len(array) == 1:
        return i
    elif target in array[: half]:
        return binary_search(target, array[: half])
    elif target in array[half:]:
        return binary_search(target, array[half:], i + half)
    return -1


print(binary_search(3, [1, 2, 3, 3, 4, 5, -3]))
