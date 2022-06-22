def main():
    total = 0
    try:
        for line in open('sales.txt'): total += float(line)
        print(f'{total:.2f}')
    except IOError:
        print('Произошла ошибка при попытке прочитать файл.')
    except ValueError:
        print('В файле найдены нечисловые данные. ')
    except:
        print('Произошла ошибка.')


main()
