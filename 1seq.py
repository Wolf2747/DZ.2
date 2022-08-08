number_of_elements = int(input('Введите колличество элементов:'))
list_elements = []
for i in range(number_of_elements):
    number = int(input('Введите число:'))
    list_elements.append(number)
list_elements.sort()
print(list_elements)
