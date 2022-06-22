def main():
    total_sum = 0
    total_num = 0
    for num in open('rand_num.txt'): total_sum += int(num); total_num += 1
    print(f'Сумма чисел: {total_sum}')
    print(f'Количество чисел: {total_num}')


main()
