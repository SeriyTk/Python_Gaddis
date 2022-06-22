def main():
    for line in open('sales.txt'): line = float(line); print(f'{line:.2f}')


main()
