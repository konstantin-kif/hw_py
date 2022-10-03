# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] 

n = int(input('input number N: '))
factorial = 1
for i in range(1, n+1):
     factorial *= i
     print(factorial, end=' ')