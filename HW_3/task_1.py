"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.
Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>
Примеры:
[2, 3, 5, 9, 3]
12
[5, 1, 5, 2, 7, 11]
14
"""
f = False
while not f:
    str = input(
        "введите элементы массива через пробел: ").split()
    f = True
    for i in str:
        if not i.isdigit():
            f = False
            print("ошибка ввода !!!")
            break
a = map(int, str)
a = list(a)

i = 1
sum = 0
while i < len(a):
    sum = sum+a[i]
    i = i+2
print(sum)
