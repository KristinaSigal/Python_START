"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""

number_of_swits = int(input('введите общее количество конфет: '))
number_in_step = int(input('введите максимальное количество, которое можно взять за один раз: '))
active_player = 1
while number_of_swits > 0:
    step_swits_number = int(input(f'Ход игрока {active_player}.\nВведите количество конфет: '))
    while step_swits_number > number_in_step or step_swits_number > number_of_swits:
        print('Ошибка')
        step_swits_number = int(input(f'Ход игрока {active_player}.\nВведите количество конфет: '))
    number_of_swits = number_of_swits-step_swits_number
    print(f'Осталось {number_of_swits} конфет')
    if number_of_swits == 0:
        print(f'Игрок {active_player} победил !!!')
    if active_player == 1:
        active_player = 2
    else:
        active_player = 1
