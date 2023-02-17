def main():
    total = 0
    quantity = 0
    with open('numbers.txt') as infile:
        for line in infile: line = float(line); total += line; quantity += 1
    print(total / quantity)

if __name__ == '__main__': main()