import csv
import var as V
import view


def Open_Date():
    result = list()
    with open(V.FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        result = list(reader)
    return result


def Get_Data():
    result = ''
    for i in Open_Date():
        result += f'{i }'
    return result


def Get_Record(soname):
    result = ''
    for i in Open_Date():
        if i['Фамилия'] == soname:
            result += f'{i }'
    return result


def Print_Data():
    view.Print_Data_View(Open_Date())


def Add_Data():
    row = view.Add_Data_View()
    Add(row)


def Add(row):
    users = Open_Date()
    Id = Get_next_Id(users)
    row['Id'] = Id
    users.append(row)
    Write_data(users)


def Del_Data():
    users = Open_Date()
    Id = view.Del_Row_View()
    row = Get_Row(users, Id)
    conf = view.Del_Conf_View(row)
    if conf == 'y':
        users.remove(row)
        Write_data(users)


def Update_Row():
    users = Open_Date()
    Id = view.Update_Row_View()
    row = users.index(Get_Row(users, Id))
    for f in users[row]:
        conf = view.Conf_View(f'{f}: {users[row][f]} изменить')
        if conf == 'Y' or conf == 'y':
            users[row][f] = view.Input_New_Val()
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
