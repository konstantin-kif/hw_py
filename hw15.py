# Вычислить число c заданной точностью d
# пример:
# при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

from math import pi

d = input('Enter the number d with the specified precision:\n'). count('0')
print(f'the number π with a given accuracy {d} = {round(pi, d)}')