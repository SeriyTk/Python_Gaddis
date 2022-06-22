def main():
    with open('sales.txt') as infile:
        line = infile.readline()
        while line != '': amount = float(line); print(f'{amount:.2f}'); line = infile.readline()

main()
