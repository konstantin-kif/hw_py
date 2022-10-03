# 2. Напишите программу для проверки
#  истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

values = False, True
print(all(not(x or y or z) == (not x and not y and not z) for x in values for y in values for z in values))
