n = int(input())
m = int(input())
k = int(input())

for i in range(1000):
    if i % m == 0 and i > k:
        n -= 1
        print(i)
    if n == 0:
        break
