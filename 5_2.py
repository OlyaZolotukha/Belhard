# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

first_number = float(input('Введите первое число: '))
action = input('Введите то, что вы хотите с ним сделать: ').replace(' ', '')
second_number = float(input('Введите второе число: '))

if action == '+':
    print(f'Наслаждайтесь результатом: ', first_number + second_number)
if action == '-':
    print(f'Наслаждайтесь результатом: ', first_number - second_number)
if action == '*':
    print(f'Наслаждайтесь результатом: ', first_number * second_number)
if action == '/':
    print(f'Наслаждайтесь результатом: ', first_number / second_number)
if action == '**':
    print(f'Наслаждайтесь результатом: ', first_number ** second_number)
if action == '//':
    print(f'Наслаждайтесь результатом: ', first_number // second_number)
if action == '%':
    print(f'Наслаждайтесь результатом: ', first_number % second_number)
