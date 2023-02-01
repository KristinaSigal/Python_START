"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи
Ввод: значение типа <int>
Вывод: значение типа <list>
Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
str = ''
while not str.isdigit():
    str = input("введите число: ")
N = int(str)
result = [1, 0, 1]
for i in range(1, N):
    result.insert(0, -result[0]+result[1])
    result.append(result[-1]+result[-2])
print(result)
