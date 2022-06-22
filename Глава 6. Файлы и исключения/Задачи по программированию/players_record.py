def add_players_record():
    with open('golf.txt', 'w') as out_file:
        while True:
            name = input('Имя игрока: ')
            if not name: break
            print(name, file=out_file)
            print(input('Счет игрока: '), file=out_file)

def show_players_record():
    with open('golf.txt') as in_file:
        while True:
            name = in_file.readline().rstrip()
            if not name: break
            else:
                check = in_file.readline().rstrip()
                print(f'Имя игрока: {name}')
                print(f'Счет игрока: {check}')

