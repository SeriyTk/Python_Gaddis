def login(par1, par2, par3):
    return par1[:3] + par2[:3] + par3[-3:]


def generate_login(par):
    print(f'Вот логин: {par}')

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
id_st = input("Введите идентификационный номер: ")
generate_login(login(first_name, last_name, id_st))
