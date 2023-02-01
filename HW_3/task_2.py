"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>
Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]
[2, 3, 5, 6]
[12, 15]
"""

import math
flag = False
while not flag:
    str = input(
        "введите элементы массива через пробел: ").split()
    flag = True
    for i in str:
        if not i.isdigit():
            flag = False
            print("ошибка ввода !!!")
            break
a = map(int, str)
New_list = list(a)
result = []
n = math.ceil(len(New_list)/2)
for j in range(0, n):
    result.append(New_list[j]*New_list[-(j+1)])
print(New_list)
print(result)
