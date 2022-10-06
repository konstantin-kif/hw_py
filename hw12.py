# Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.20

from random import randint

number = int(input('Enter the size of the list: '))
list = []
for i in range(number):
    list.append(float(randint(0, 9)))
    
min = list[0]
max = 0
for i in range(len(list)):
    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
difference = (max - min)

print(list)
print(float(difference))
