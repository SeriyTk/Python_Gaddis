def main():
    total = 0
    for i in open('number_list.txt'): total += int(i)
    print(total, sep='')


main()
