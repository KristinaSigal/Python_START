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
    users = list(Open_Date())
    with open(V.FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=V.FILDS)
        for f in V.FILDS:
            row[f] = input(f'{f} : ')
        print(row)
        users.append(row)
        writer.writeheader()
        writer.writerows(users)
