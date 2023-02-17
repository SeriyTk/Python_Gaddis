def sales_report1():
    total = 0
    try:
        with open('sales_data.txt') as infile:
            for line in infile: amout = float(line); total += amout
        print(f'{total:,.2f}')
    except IOError: print ('Произошпа ошибка при попытке прочитать файл.')
    except ValueError: print ('В файле найдены не числовые данные.' )
    except: print('Произошпа ошибка.')

if __name__ == '__main__': sales_report1()