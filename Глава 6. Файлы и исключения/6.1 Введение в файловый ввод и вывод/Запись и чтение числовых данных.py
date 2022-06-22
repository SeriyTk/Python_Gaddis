def main():
    with open('numbers.txt', 'w') as outfile:
        for i in range(3): print(input(f'Введите число №{i + 1}: '), file=outfile)

main()

def main1():
    total = 0
    for i in open('numbers.txt'): total += int(i)
    print(int(total))

main1()
