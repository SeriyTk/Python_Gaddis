def main():
    with open('my_name.txt', 'w') as out_file: print(input('Ваше имя: '), file=out_file)


main()
