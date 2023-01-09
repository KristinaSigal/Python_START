import csv
import var as V


def Open_Date():
    result = list()
    with open(V.FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        result = list(reader)
    return result


def Print_Data():
    from tabulate import tabulate
    print(tabulate(Open_Date(), headers="keys", tablefmt="fancy_grid"))


def Add_Data():
    row = dict()
    for f in V.FILDS[1:]:
        row[f] = input(f'{f} : ')
    users = Open_Date()
    Id = Get_next_Id(users)
    row['Id'] = Id
    users.append(row)
    Write_data(users)


def Del_Data():
    users = Open_Date()
    Id = input('Введите Id записи для удаления :')
    row = Get_Row(users, Id)
    print(f'Вы хотите удалить запись: { row } ?')
    conf = input('Да : y  Нет : n ? ')
    if conf == 'y':
        users.remove(row)
        Write_data(users)


def Update_Row():
    users = Open_Date()
    Id = input('Введите Id записи для изменения :')
    row = users.index(Get_Row(users, Id))
    for f in users[row]:
        conf = input(f'{f}: {users[row][f]} изменить  (y/n)?')
        if conf == 'y':
            users[row][f] = input(
                'Введите новое занчение:')
    from tabulate import tabulate
    print(tabulate(users, headers="keys", tablefmt="fancy_grid"))
    Write_data(users)


def Get_Row(users, Id):
    return next(x for x in users if x['Id'] == Id)


def Get_next_Id(users):
    maxId = 0
    for r in users:
        if maxId < int(r['Id']):
            maxId = int(r['Id'])
    return maxId+1


def Write_data(users):
    with open(V.FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=V.FILDS)
        writer.writeheader()
        writer.writerows(users)
