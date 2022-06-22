def main():
    total = 0
    try:
        for line in open('sales.txt'): total += float(line)
        print(f'{total:.2f}')

    except:
        print('Произошла ошибка.')


main()
