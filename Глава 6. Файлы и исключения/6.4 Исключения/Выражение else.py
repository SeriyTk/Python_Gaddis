def main():
    total = 0
    try:
        for line in open('sales.txt'): total += float(line1)
    except Exception as err:
        print(err)
    else:
        print(f'{total:.2f}')


main()
