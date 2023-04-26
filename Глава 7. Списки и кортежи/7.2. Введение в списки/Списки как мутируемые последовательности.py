numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[0] = 99
print(numbers)
print()
NUM_DAYS = 5
def main():
    sales = [i for i in range(NUM_DAYS)]
    print('Введите продажи за каждый день.')
    for index in range(len(sales)): sales[index] = float(input(f'День №{index + 1}: '))
    print('Вот значения, которые были введены: ')
    for value in sales: print(value)

if __name__ == '__main__': main()