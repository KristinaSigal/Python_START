"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""

def sum(a, b): return a + b
def dif(a, b): return a - b
def mult(a, b): return a * b
def div(a ,b): return a / b

def make_operation(a,b,op):
    if op == '+': operation = sum
    if op == '-': operation = dif
    if op == '*': operation = mult
    if op == '/': operation = div
    return operation(a, b)

#выполнение операции в списке
def make_operation_in_list(lst, i):
    lst[i] = str(make_operation(float(lst[i - 1]), float(lst[i + 1]), lst[i]))
    lst.pop(i - 1)
    lst.pop(i)

#расчет выражения без скобок
def parcCalc(mas):
   # mas = exp.split(' ')
    while '*' in mas or '/' in mas or '+' in mas or '-' in mas:
        while '*' in mas:
            i = mas.index('*')
            make_operation_in_list(mas, i)
        while '/' in mas:
            i = mas.index('/')
            make_operation_in_list(mas, i)
        while '+' in mas:
            i = mas.index('+')
            make_operation_in_list(mas, i)
        while '-' in mas:
            i = mas.index('-')
            make_operation_in_list(mas, i)
    return mas[0]

#раскрытие скобок
def open_paren(lst):
    while '(' in lst or ')' in lst:
        flag = False
        i = 0
        while not flag and i < len(lst):
            if lst[i] == '(':
                start_index = i
            i+=1
            if lst[i] == ')':
                end_index = i
                flag = True
        print(lst[start_index+1: end_index])
        lst[start_index] = parcCalc(lst[start_index+1: end_index])
        for j in range(start_index+1, end_index+1):
            lst.pop(start_index+1)
    print( parcCalc(lst))

open_paren('2 + ( ( 3 + 5 ) / 4 - 1 ) + ( 6 + 4 ) / 2'.split(' '))
