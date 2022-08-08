str_number = input('Введите числа через запятую')
numbers = str_number.split(',')
str_number = input('Введите числа через запятую')
numbers_too = str_number.split(',')

for number in numbers[:]:
    if number in numbers_too:
        numbers.remove(number)
print(numbers)