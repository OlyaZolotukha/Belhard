# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

dicti = {
    'Belarus': ['Minsk', 'Vitebsk', 'Gomel', 'Brest'],
    'Russia': ['Moscow', 'Saint Petesburg', 'Kursk', 'Vladivostok'],
    'United States': ['New York', 'Washington', 'Los Angeles', 'Las Vegas']
}
a = input('Введите название города: ').title()


def get_key(dicti, value):
    for i in range(len(dicti.values())):
        for k, v in dicti.items():
            if v[i] == value:
                return k


print(get_key(dicti, a))
