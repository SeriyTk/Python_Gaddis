def main():
    with open('philosophers.txt', 'w') as outfile:
        for i in range(3): print(input('Имя: '), file=outfile)


main()
