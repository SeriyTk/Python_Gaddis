def main():
    total_sum = 0
    total = 0
    for number in open('numbers.txt'): total_sum += int(number); total += 1
    print(f'Среднее арифметическое: {total_sum / total}')


main()
