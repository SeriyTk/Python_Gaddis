print(open('philosophers.txt').read())
print()
for i in open('philosophers.txt'): print(i, end='')
print()

def main():
    with open('philosophers.txt') as infile:
        line1 = infile.readline().rstrip()
        line2 = infile.readline().rstrip()
        line3 = infile.readline().rstrip()

        print(line1)
        print(line2)
        print(line3)
main()