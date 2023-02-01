"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""

import random

n = int(input("Введите степень полинома: "))
result = ""
while n > 0:
    k = random.randint(0, 10)
    if k != 0:
        if k > 1:
            result = result + f"{k}*"
        if n > 1:
            result = result + f"x^{n}+"
        else:
            result = result + f"x+"
    n -= 1
k = random.randint(0, 10)
if k != 0:
    result = result + f"{k}=0"
else:
    result = result + "=0"
f = open('polinom.txt', 'w')
f.write(result)
print(f'полином {result}')
