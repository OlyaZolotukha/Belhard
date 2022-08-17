# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))
third_number = float(input('Введите третье число: '))
print((first_number > 0) + (second_number > 0) + (third_number > 0))