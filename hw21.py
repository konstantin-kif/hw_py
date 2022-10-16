# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

total_candy = 28

def human_turn(player, count):
    while True:
         candies_sum = int (input(f'\n Введите сколько конфет берет игрок: {player}: '))
         if 1 <= candies_sum <= total_candy:
            count -= candies_sum
            print(f'Осталось {count} конфет: ')
            return count
        else:
            print(f'\nБольше {total_candy} конфеты за ход брать нельзя!\n')
            
def computer_bot_turn(count, difficult):
    candies_sum  = random.randint(1, total_candy)
    if difficult:
        candies_sum = count % (total_candy + 1) if  candies_sum == 0 else  candies_sum
    print(f'\n Компьютер берет { candies_sum} кофет')
    count -+  candies_sum
    print(f'Осталось {count} конфет')
    return count

candies_count = 2021
print(f'Добро пожаловать в игру  "{candies_count} конфета!"')
opponent = int(input('Выберете соперника: "1" - Человек, "2" - Коьпьютер: \n'))

if opponent == 1:
    player_1 = input('Введите имя игрока 1: ')
    player_2 = input('Введите имя игрока 2: ')
    print(f'Перед Вами {candies_count} конфета. За один ход можно забрать не больше чем {total_candy} конфеты')
    current_player = random.choice([player_1, player_2])
    print(f'\nПроведем жеребьевку!\nПервый ход делает игрок {current_player}\n ')

    while True:
        candies_count = human_turn(current_player, candies_count)
        current_player = player_2 if current_player == player_1 else player_1
        if 0 <= candies_count <= total_candy:
            break
    print(f'\nПобедил игрок {current_player}!\nПоздровляем!!! ')

elif opponent == 2:
    player_1 = input('Введите имя игрока 1: ')
    player_2 = 'Компьютер'
    print(f'Перед Вами {candies_count} конфета. За один ход можно забрать не больше чем {total_candy} конфеты')
    current_player = random.choice([player_1, player_2])
    print(f'\nПроведем жеребьевку!\nПервый ход делает игрок {current_player}\n ')

    difficulty_level = int(input('Выберете уровень сложности игры: "1" - легкий, "2" - сложный: \n'))
    difficulty_level = True if difficulty_level == 2 else False

    while True:
        if current_player == player_1:
            candies_count = human_turn(current_player, candies_count)
            current_player = player_2 if current_player == player_1 else player_1
        else:
             candies_count = computer_bot_turn(candies_count, difficulty_level)
             current_player = player_2 if current_player == player_1 else player_1
        if 0 <= candies_count <= total_candy:
            break
    print(f'\nПобедил игрок {current_player}!\nПоздровляем!!! ')
else:
    print ('Некорректный ввод. Поробуй войти в игру еще раз!')
