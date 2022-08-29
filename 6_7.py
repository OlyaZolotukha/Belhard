# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
numbers = [1, 2, 3, 4, 5, 6, 7]


for i in range(len(numbers)):
    if i == 0:
        i = numbers[len(numbers) - 1] + numbers[1]
    elif i == len(numbers) - 1:
        i = numbers[len(numbers) - 2] + numbers[0]
    else:
        i = numbers[i - 1] + numbers[i + 1]
    print(i)