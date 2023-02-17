def main():
    total = 0
    with open('numbers.txt') as infile:
        for line in infile: line = float(line); total += line
    print(total)

if __name__ == '__main__': main()