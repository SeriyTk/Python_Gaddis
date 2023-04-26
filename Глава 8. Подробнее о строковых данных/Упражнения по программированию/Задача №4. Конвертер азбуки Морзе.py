def main():
    with open('Morse_code_rus.csv') as csv_file:
        lines = csv_file.readlines()
        str_line = input(': ')
        for letter in str_line:
            for line in lines:
                line = line.rstrip().split(',')
                if line[0] == letter.lower() or line[0] == letter.upper(): print(line[1], end=' ')
                else: continue



if __name__ == '__main__': main()