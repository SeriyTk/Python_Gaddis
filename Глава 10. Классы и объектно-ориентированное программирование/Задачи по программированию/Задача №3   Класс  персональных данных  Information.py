import info

def main():
    name, address, phone = info.personal_data()
    my_info = info.Information(name, address, phone)
    name, address, phone = info.personal_data()
    friends1 = info.Information(name, address, phone)
    name, address, phone = info.personal_data()
    friends2 = info.Information(name, address, phone)
    print()
    print('Информация обомне.')
    print(my_info)
    print('---------------------------------------------------------------------------------')
    print('Информация о друзьях.')
    print(friends1)
    print(friends2)


if __name__ == '__main__': main()