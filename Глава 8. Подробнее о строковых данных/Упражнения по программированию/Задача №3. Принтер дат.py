def main():
    date = input('Введите дату: ')
    tokens = date.split('/')
    for token in tokens: print(token, end=' ')

if __name__ == '__main__': main()