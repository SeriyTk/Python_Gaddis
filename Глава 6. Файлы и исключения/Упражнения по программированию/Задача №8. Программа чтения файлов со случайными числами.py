def main():
    sum = 0
    total = 0
    with open('rand_numbers.txt') as infile:
        for line in infile: line = int(line); sum += line; total += 1
    print(f'Сумма чисел: {sum}, всего чисел: {total}')

if __name__ == '__main__': main()