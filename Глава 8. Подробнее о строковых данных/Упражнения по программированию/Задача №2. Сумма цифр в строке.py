def main():
    str  = input('Введите цифры: ')
    total = 0
    for item in  range(len(str)):
        total += int(str[item])
    print(total)

if __name__ == '__main__': main()