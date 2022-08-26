line_1 = input()
line_2 = input()
count_line = 0

if len(line_1) >= len(line_2):

    for i in range(len(line_2)):
        if line_1[i] == line_2[i]:
            count_line += 1
    print(count_line)

if len(line_1) < len(line_2):

    for i in range(len(line_1)):
        if line_1[i] == line_2[i]:
            count_line += 1
    print(count_line)
