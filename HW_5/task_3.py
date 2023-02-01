"""
Напишите игру "Крестики-нолики".
"""

def print_pole(pole):
    print('   | A | B | C |')
    print('---|---|---|---|')
    row_num = 0
    for row in pole:
        row_num += 1
        print(f'{row_num}  ', end='|')
        for cel in row:
            print(f' {cel} ', end='|')
        print('\n---|---|---|---|')


#Сообщение о победе
def victory_message(mark):
    print (f'ПОБЕДА {mark} !!!')

# проверка линии
def check_line(line):
    if line[0] != ' ' and line[0] == line[1] and line[1] == line[2]:
        victory_message(line[0])
        return True

# получение солонки
def get_column(pole, columnNamber):
    return [pole[0][columnNamber], pole[1][columnNamber], pole[2][columnNamber]]

# получение первой диагонали
def get_diagonal1(pole):
    return [pole[0][0], pole[1][1], pole[2][2]]

# получение второй диагонали
def get_diagonal2(pole):
    return [pole[0][2], pole[1][1], pole[2][0]]

# проверка выйгрыша
def chesk_pole(pole):
    for row in pole:
        if check_line(row):
            return True
    for column in range(0, 3):
        if check_line(get_column(pole, column)):
            return True
    if check_line(get_diagonal1(pole)):
        return True
    if check_line(get_diagonal2(pole)):
        return True
    return False

#запись значения
def set_mark(input_string, mark, pole):
    x = -1
    if input_string[0] == 'A':
        x = 0
    if input_string[0] == 'B':
        x = 1
    if input_string[0] == 'C':
        x = 2
    y = -1
    if input_string[1] == '1':
        y = 0
    if input_string[1] == '2':
        y = 1
    if input_string[1] == '3':
        y = 2
    if x != -1 and y != -1 and pole[y][x] == ' ':
        pole[y][x] = mark
        print_pole(pole)
    else:
        print(f'ПОЛЕ {input_string} ЗАНЯТО !!!')
        step(mark, pole)

#ввод
def step(mark, pole):
    input_string = input(f'сделайте ход [{mark}]: ')
    while (not input_string[0] in ['A', 'B', 'C']) or (not input_string[1] in ['1', '2', '3']):
        print('ОШИБКА !!!')
        input_string = input('сделайте ход: ')
    set_mark(input_string, mark, pole)

#Игровой цикл
def igra(pole):
    mark = 'X'
    step_number = 0
    while (step_number < 9) and not (chesk_pole(pole)):
        if mark == 'X':
            mark = 'O'
        else: mark = 'X'
        step(mark, pole)
        step_number += 1
    if step_number == 9:
        print('НИЧЬЯ !!!')

p = [
     [' ', ' ', ' '],
     [' ', ' ', ' '],
     [' ', ' ', ' ']
                    ]
print_pole(p)
igra(p)

