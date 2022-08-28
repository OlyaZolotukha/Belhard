massive1 = []
massive2 = []
super_puper_massive = []

codename = input('')

for i in range(len(codename)):
    char = bin(ord(codename[i]))[2:]
    char = '0' * (8 - len(char)) + char
    massive1 = massive1 + [char]
print(massive1)

key_word = input()

for j in range(len(key_word)):
    char = bin(ord(key_word[j]))[2:]
    char = '0' * (8 - len(char)) + char
    massive2 = massive2 + [char]
print(massive2)

for t in range(len(massive1)):
    g = []
    g.clear()
    for v in range(len(massive1[t])):
        if massive1[t][v] == massive2[t][v]:
            g += [0]
        else:
            g += [1]

    super_puper_massive.append(g)


print(super_puper_massive)
