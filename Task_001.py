# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import random
from random import randint

num_game, stroke_size = 2021, 28
num_gamer_1, num_gamer_2, count = 0, 0, 0
count_1, count_2 = 0, 0


for count_1 in range(num_game // 2):
    count += 1
    num_gamer_1 = int(input(f'Введите количество конфет для {count} хода (от 1 до 28):'))
    if 1 > num_gamer_1 or num_gamer_1 > 28:
        print('Вы ввели не корректное число, начните сначала.')
        break
    else:
        num_game = num_game - num_gamer_1
        if num_game == 0:
            print('Вы победили!')
            break
        else:
            print(f'Осталось {num_game} конфет')
        if num_game <= 28:
            num_gamer_2 = num_game
            num_game = num_game - num_gamer_2
        else:
            num_gamer_2 = randint(1, 28)
            num_game = num_game - num_gamer_2
            print(f'Ход соперника {count}: {num_gamer_2}')
        if num_game == 0:
            print("Вы проиграли(")
            break
        else:
            print(f'Осталось {num_game} конфет')

