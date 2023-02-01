"""
Реализуйте RLE алгоритм шифрования строки: замените повторяющиеся символы строки на один символ и число его повторов.
На первом месте идет количество повторов, на втором сам символ.
Восстановите строку после шифрования.

Ввод: значения типа <str>, можно получить из файла.
Вывод: значение типа <str>, можно записать в файл.

Примеры:
ыыыыыррррр   аааааагггггггг
5ы5р3 6а8г
"""

import re

initial_string = input(
    f'введите строку для кодирования:')
char = initial_string[0]
number_of_char = 1
serial_nuber = 1
result = ''
for nC in range(1, len(initial_string)):
    if initial_string[nC] == initial_string[nC-1]:
        serial_nuber += 1
    else:
        result = result + f'{serial_nuber}{initial_string[nC-1]}'
        serial_nuber = 1
result = result + f'{serial_nuber}{initial_string[len(initial_string)-1]}'
print(result)
split_result = re.findall('\d+\D', result)
repair_string = ''
for clausa in split_result:
    nChar = int(re.search('\d+', clausa)[0])
    char = re.search('\D', clausa)[0]
    repair_string = repair_string + char * nChar
print(repair_string)
