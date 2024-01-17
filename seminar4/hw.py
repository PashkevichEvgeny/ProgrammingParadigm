def a(arr):
    return map(lambda x: x - sum(arr) / len(arr), arr)


def b(arr):
    return sum(map(lambda x, : x ** 2, a(arr))) ** 0.5


def correlation_pearson(arr_x, arr_y):
    denominator = b(arr_x) * b(arr_y)
    if denominator == 0:
        return 0
    return sum(map(lambda x, y: x * y, a(arr_x), a(arr_y))) / denominator
