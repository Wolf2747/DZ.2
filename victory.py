import random
people = {
    'Киллиан Мерфи': '25.05.1976',
    'Анджелина Джоли': '04.06.1975',
    'Том Харди':'15.09.77',
    'Том Круз': '03.07.1962',
    'Эмма Уотсон': '15.04.1990',
    'Дениэл Редклифa': '23.07.1989',
    'Харрисон Форд': '13.07.1942',
    'Юэн Макгрегор': '31.03.1971',
    'Натали Портман': '09.06.1981',
    'Марк Уолберг': '05.06.1971'
}
days = {
    '25': 'двадцать пятое',
    '04': 'четвертое',
    '15': 'пятнадцатое',
    '03': 'третье',
    '23': 'двадцать третье',
    '13': 'тринадцтое',
    '31': 'тридцать первое',
    '09': 'девятое',
    '05': 'пятое'
}
months = {
    '05': 'мая',
    '06': 'июня',
    '09': 'сентября',
    '07': 'июля',
    '04': 'апреля',
    '03': 'марта'

}
reset = ' '
while reset != 'нет':
    right = 0
    wrong = 0
    for i in range (5):
        people.copy()
        name = random.choice(list(people.keys()))
        print(name)
        answer = input('Введите дату рождения:')
        if people[name] == answer:
            right += 1

        else:
            data = people[name]
            day, month, year = data.split('.')
            print(days[day],months[month],year, 'года')
            wrong += 1
        people.pop(name)
    print('Верно', right)
    print('неверно', wrong)
    reset = input('Хотите пройти заново?')