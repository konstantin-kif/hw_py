# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

number = int(input('Enter a natural number N: '))
factors = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        factors.append(i)
        number /= i
if number > 1:
    factors.append(int(number))
print(f'List of prime factors of a number {number}: {factors}')
