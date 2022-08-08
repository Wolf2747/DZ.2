str_number = input('Введите числа через запятую')
numbers = str_number.split(',')
result = []
for i in numbers:
    if numbers.count(i) == 1:
        result.append(i)
print(result)



