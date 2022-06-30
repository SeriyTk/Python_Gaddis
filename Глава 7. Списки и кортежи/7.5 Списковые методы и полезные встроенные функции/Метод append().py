def main():
    name_list = []
    while True:
        name = input('Введите имя: ')
        if not name: break
        else: name_list.append(name)
    print()
    for name in name_list: print(name)

main()
