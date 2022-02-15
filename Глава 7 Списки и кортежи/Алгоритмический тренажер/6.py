def search_name():
    search_name = input('Кого ищем? ')
    with open(r'G:\students.txt') as name_file:
        if search_name in name_file.read().replace('\n',' '):
            print(f'Привет {search_name}.')
        else:
            print(f'{search_name} нету дома.')
            


search_name()
