import model as M
import var as V


def work():
    operation = 0
    while operation != 5:
        operation = int(input(V.MENU))
        if operation == 1:
            M.Print_Data()
        if operation == 2:
            M.Add_Data()
        if operation == 3:
            M.Del_Data()
        if operation == 4:
            M.Update_Row()
        if operation == 5:
            M.Get_Data()
