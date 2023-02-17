def main():
    total = 1
    with open('numbers.txt') as infile:
        for num in infile:
            if total <= 2: print(num.rstrip()); total += 1

if __name__ == '__main__': main()