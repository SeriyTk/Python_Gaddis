def main():
    my_string = 'Один два три четыре'
    word_list = my_string.split()
    print(word_list)

    if __name__ == '__main__': main()
def main():
    date_string = '26/11/2020'
    date_list = date_string.split('/')
    print(f'Дeнь: {date_list[0]}')
    print(f'Mecяц: {date_list[1]}')
    print(f'Гoд: {date_list[2]}')

if __name__ == '__main__': main()