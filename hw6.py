# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

sum_numbers = input('input number: ')
sum = 0
for i in sum_numbers:
    if i != '.':
        sum += int(i)
print(round(sum))