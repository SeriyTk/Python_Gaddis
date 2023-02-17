def main():
    num = 0
    with open('numbers.txt') as infile:
        for line in infile: print(f'Строка №{num +1}: {line.rstrip()}'); num += 1

if __name__ == '__main__': main()