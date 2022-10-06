# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Enter the size of the Fibonacci number: '))
if number < 0:
    number = number * -1
f1 = f2 = 1
list = [f1, f2]
for i in range(2, number):
    f1, f2 = f2, f1 + f2
    list.append(f2)
f1 = f2 = 1
for i in range(-number, 1):
    f1, f2 = f2, f1 - f2
    list.insert(0, f2)
print(list)
