'''for переменная in файловый_ объект:
    инструкция
    инструкция
    . . .
    '''
def read_sales():
    with open('sales.txt') as sales_file:
        for line in sales_file: amount = float(line); print(f'{amount:.2f}')

if __name__ == '__main__': read_sales()