def read_sales():
    with open('sales.txt') as sales_file:
        while True:
            line = sales_file.readline()
            if line != '':
                amount = float(line)
                print(f'{amount:.2f}')
            else: break

if __name__ == '__main__': read_sales()