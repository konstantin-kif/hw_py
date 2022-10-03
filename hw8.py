# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('input n: '))
def sequence(n):
    return [((1 + 1 / n) ** n) for i in range (1, n + 1)]       
print(sum(sequence(n)))
