def file_write():
    with open('philosophers .txt') as infile: file_contents = infile.read(); print(file_contents)

if __name__ == '__main__': file_write()
print()
def line_read():
    with open('philosophers .txt', 'r') as infile:
        line1 = infile.readline()
        line2 = infile.readline()
        line3 = infile.readline()

        print(line1)
        print(line2)
        print(line3)

if __name__ == '__main__': line_read()