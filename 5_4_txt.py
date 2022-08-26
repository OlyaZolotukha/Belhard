# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

list_1 = [4, 5, 8, 3, 1, 6, 9, 2]
a = 0

for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if list_1[i] > list_1[j]:
            a = list_1[i]
            list_1[i] = list_1[j]
            list_1[j] = a
print(list_1)
