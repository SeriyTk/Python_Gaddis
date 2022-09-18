import employee as empl

def main():
    e_list = empl.employee_list()
    print("Имя \t Идентификационный номер \t Отдел \t Должность")
    print("--------------------------------------------------------------------")
    empl.display_employee(e_list)



if __name__ == '__main__': main()