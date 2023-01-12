import var


def Add_Data_View():
    row = dict()
    for f in var.FILDS[1:]:
        row[f] = input(f'{f} : ')
    return row


def Del_Row_View():
    return input('Введите Id записи для удаления :')


def Del_Conf_View(Id):
    print(f'Вы хотите удалить запись: { Id } ?')
    return input('Да : y  Нет : n ? ')


def Print_Data_View(data):
    from tabulate import tabulate
    print(tabulate(data, headers="keys", tablefmt="fancy_grid"))


def Update_Row_View():
    return input('Введите Id записи для изменения :')


def Conf_View(message):
    return input(f"{message} (Y/N):")


def Input_New_Val():
    return input('Введите новое занчение:')
