# return  выражение1,  выражение2, ...
def get_name():
    f_name = input('Имя: ')
    l_name = input('Фамилия: ')
    return f_name, l_name

first_name, last_name = get_name()
print(f'Имя:{first_name}, фамилия: {last_name}.')