"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""

data = list(map(int, input().split(',')))
singleResult = list()
for i in data:
    if data.count(i) == 1:
        singleResult.append(i)
uniqResult = list(set(data))
repeatResult = list(set(data).difference(set(singleResult)))
print(singleResult)
print(repeatResult)
print(uniqResult)
