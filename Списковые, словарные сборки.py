def odd_square(num):
    square = num ** 2
    if square % 2 != 0:
        return square


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = list(filter(lambda x: x is not None, map(odd_square, numbers)))

print(result)
