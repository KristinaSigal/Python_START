"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""

string = input('Введите строку:')
mas_string = string.split(' ')
result = ''
for i in mas_string:
    exist = ("a" in i) or ("б" in i) or ("в" in i)
    if not exist:
        result = result+' '+i
print(result)
