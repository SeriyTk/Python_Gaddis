def main():
    def write_file():
        while True:
            enter = input('Ввести имя игрока? ')
            if enter != '': print('Запись создана.'); break
            else:
                with open('golf.txt', 'a') as outfile:
                    name = input('Имя: ')
                    check = input('Счет: ')
                    outfile.write(f'{name}\n')
                    outfile.write(f'{check}\n')
    #write_file()
    def read_file():
        with open('golf.txt') as infile:
            for line in infile: print(line.rstrip())
    read_file()

if __name__ == '__main__': main()