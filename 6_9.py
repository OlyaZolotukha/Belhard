#Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
#словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
#имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
#пустая строка)

dicti = dict(ID123={
    'name': 'Petr',
    'surname': 'Ivanov',
    'telephone': '101',
    'email': 'ivanov@mail.ru'
}, ID456={
    'name': 'Maria',
    'surname': 'Ivanova',
    'telephone': '102',
    'email': None
}, ID789={
    'name': 'Oksana',
    'surname': 'Ivanova',
    'telephone': '103',
})

def get_key(dicti):
    for k, v in dicti.items():
        if v.get('email') is None:
            print(k)

get_key(dicti)
