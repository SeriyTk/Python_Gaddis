def main():
    with open('numbers.txt') as infile:
        for num in infile: print(num.rstrip())

if __name__ == '__main__': main()