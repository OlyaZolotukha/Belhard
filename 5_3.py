# **Вывести четные числа от 2 до N по 5 в строку

n = int(input())

for i in range(2, n+1):
    if i % 2 == 0:
        print(i, end=' ')
    if i % 10 == 0:
        print('')
