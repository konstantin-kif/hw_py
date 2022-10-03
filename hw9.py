# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

def fill_list(n: int) -> list: 
    new_list = [random.randint(-n, n)]
    for i in range(1, n):
        new_list.append(random.randint(-n, n))
        i += 1
    return new_list

def writing_file(k: int, n: int):
   with open('file.txt', 'w') as position:
       for i in range(k):
           position.write(f'{random.randint(0, n-1)}\n')

def print_position():
   path = 'file.txt'
   position = open(path, 'r')
   pos_element = []
   for line in position:
    pos_element.append(int(line))
   print(f'Позиции элементов: {pos_element}')
   position.close()
   return pos_element

def product_elements(user_list: list, k: int) -> int:
   path = 'file.txt'
   position = open(path, 'r')
   product = 1
   for line in position:
    product = product * user_list[int(line)]
   position.close()
   return product

n = int(input('Количество элементов: N = '))
new_list = fill_list(n)
k = int(input('Количество множителей: k = '))
writing_file(k, n)
print(f'Заданный список: {new_list}')
print_position()
print(f'Произведение элементов на заданных позициях равно {product_elements(new_list, k)}')