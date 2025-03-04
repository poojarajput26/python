def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5, 6]
deep = map(square, numbers)
print(list(deep))  # [1, 4, 9, 16, 25]
