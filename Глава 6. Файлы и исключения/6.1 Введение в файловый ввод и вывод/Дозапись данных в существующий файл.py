def main():
    with open('friends.txt', 'a') as outfile:
        while True:
            enter = input('Нет: ')
            if enter == "нет":
                break
            else:
                print(input('Имя: '), file=outfile)


main()
