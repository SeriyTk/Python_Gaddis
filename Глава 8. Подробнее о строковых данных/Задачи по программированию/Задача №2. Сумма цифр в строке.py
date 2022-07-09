def main():
    numers = int(input('Число: '))
    num1 = numers // 1000
    num2 = (numers // 100) % 10
    num3 = (numers // 10) % 10
    num4 = numers % 10
    total = num1 + num2 + num3 + num4
    print(total)


main()
