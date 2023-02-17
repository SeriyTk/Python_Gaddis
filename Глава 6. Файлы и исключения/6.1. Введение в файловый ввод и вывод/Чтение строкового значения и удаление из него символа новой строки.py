def strip_newline():
    with open('philosophers .txt') as infile:
        line1 = infile.read().rstrip()
        line2 = infile.read().rstrip()
        line3 = infile.read().rstrip()

        print(line1)
        print(line2)
        print(line3)

if __name__ == '__main__': strip_newline()
