"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""


def prime_numbers(n):
    result = list(range(2, n + 1))
    i = 1
    p = result[i]
    while i < len(result):
        j = i + 1
        while j < len(result):
            if result[j] % result[i] == 0:
                result.pop(j)
            else:
                j += 1
        i += 1
    return result


def get_prime_mult(n):
    mult = prime_numbers(n // 2)
    result = []
    ost = n
    flag = True
    while ost > 1 and flag:
        i = 0
        flag = False
        while i < len(mult) and ost >= mult[i]:
            if ost % mult[i] == 0:
                ost = ost // mult[i]
                result.append(mult[i])
                flag = True
                break
            else:
                i += 1
    if flag:
        print(f"Множители: {result}")
    else:
        print("Простых множителей нет")


get_prime_mult(int(input("Введите число:")))
