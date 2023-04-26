def main():
    with open('alphabetical_number.csv') as cvs_file:
        numbers = input('Введите номер телефона: ')
        lines = cvs_file.readlines()
        for num in numbers:
            if num.isdigit(): print(num,end='')
            for line in lines:
                line = line.rstrip().split(',')
                if line[0] == num.lower() or line[0] == num.upper(): print(line[1], end='')

if __name__ == '__main__': main()