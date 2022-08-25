a = int(input())
line = []

for i in range(a):
    line = [1] + line
    for i in range(1, len(line) - 1):
        line[i] += line[i + 1]
    print(line)
