def main():
    with open('sales.txt','w') as sales_file:
        for count in range(int(input('Количество дней: '))):
            print(float(input(f'Введите продажи за день №{count + 1}: ')), file=sales_file)


main()
