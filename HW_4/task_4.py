"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""

import re


def pars_polinom(s):  # разбор полинома
    s = s.replace('-', '+-')
    print(s)
    match = re.split('\+|=', s)
    num = dict()
    for i in match:
        # выбираем коэффициенты
        k = re.search(r'^-?\d*', i)
        K = k[0] if k else '1'
        d = re.search(r'(x\^)\d*', i)  # выбираем степени
        if d:
            D = int(re.search(r'\d+', d[0])[0])
        else:
            d = re.search(r'x', i)
            if d:
                D = 1
            else:
                D = 0
        if D in num:
            num[D] = num[D]+int(K)
        else:
            num[D] = int(K)
    return (num)


def sum_polinom(a, b):  # сложение полиномов
    sum = dict()
    keys = list(a.keys())
    keys.extend(b.keys())
    maxDegree = max(keys)
    for i in range(maxDegree+1):
        if (i in b) and (i in a):
            sum[i] = a[i]+b[i]
        elif i in a:
            sum[i] = a[i]
        elif i in b:
            sum[i] = b[i]
    result = ""
    flag = True
    y = sorted(sum, reverse=True)
    for i in sorted(sum, reverse=True):
        plus = '+'
        if flag or sum[i] < 0:
            plus = ''
            flag = False
        degree = ''
        if i > 1:
            degree = f"*x^{i}"
        elif i == 1:
            degree = f"*x"
        else:
            degree = f""
        result = result + f"{plus}{sum[i]}{degree}"
    return result+"=0"


# a='9x^5+7x^4+7x^3+9x^2+6x+17=0'
# b='3x^2+2x+1=0'
f = open('polinomA.txt', 'r')
a = f.readline()
f.close()
f = open('polinomB.txt', 'r')
b = f.readline()
f.close()
f = open('polinom_sum.txt', 'w')
sumP = sum_polinom(pars_polinom(a), pars_polinom(b))
f.write(sumP)
f.close()
print(sumP)
