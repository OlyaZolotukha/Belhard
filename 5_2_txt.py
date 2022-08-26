list_1 = '12345'
list_2 = 'qwerty'
list_3 = 'minsk city'
list_4 = 'avada kedavra'
count_list = 0


paginator3000 = [list_1, list_2, list_3, list_4]
print(paginator3000[count_list])
while 1:
    button = input()
    if button == '>':
        count_list += 1
        if count_list == len(paginator3000):
            count_list = 0
        print(paginator3000[count_list])
        continue
    elif button == '<':
        if count_list == 0:
            count_list = len(paginator3000)
        count_list -= 1
        print(paginator3000[count_list])
        continue
