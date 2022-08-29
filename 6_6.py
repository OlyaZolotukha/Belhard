# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётные

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = list(filter(lambda x: x % 2 == 0, numbers)) + list(filter(lambda x: x % 2, numbers))
print(numbers)
