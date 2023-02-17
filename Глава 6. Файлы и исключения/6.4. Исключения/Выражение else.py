'''
try:
    инструкция
    инструкция
    . . .
except ИмяИсключения:
    инструкция
    инструкция
    . . .
else:
    инструкция
    инструкция
    . . .
'''
def sales_report():
    total = 0
    try:
        with open('sales_data.txt') as infile:
            for line in infile: amount = float(line); total += amount
    except Exception as err: print(err)
    else: print(f'{total:,.2f}')


if __name__ == '__main__': sales_report()