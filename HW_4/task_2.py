"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>

Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

import random

N = int(input("Введите длинну массива:"))
mas = []
for i in range(0, N):
    mas.append(random.randint(0, 10))
result = []
for i in mas:
    if mas.count(i) == 1:
        result.append(i)
print(mas)
print(result)
