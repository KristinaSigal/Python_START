"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>
Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
import random
import sys
flag = False
while not flag:
    str = input(
        "введите элементы массива через пробел: ").split()
    flag = True
    for i in str:
        if len(i.split('.')) < 3:
            for j in i.split('.'):
                if not j.isdigit():
                    flag = False
                    print("ошибка ввода !!!")
                    break
        else:
            flag = False
            print("ошибка ввода !!!")
a = map(float, str)
New_list = list(a)
max = sys.float_info.min
min = sys.float_info.max
for j in New_list:
    if (max < j % 1):
        max = j % 1
    if (min > j % 1):
        min = j % 1
print(round(max-min, 2))
