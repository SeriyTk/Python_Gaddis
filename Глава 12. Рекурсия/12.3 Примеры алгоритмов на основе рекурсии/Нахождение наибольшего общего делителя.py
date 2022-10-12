def main():
    num1 = int(input('Введите целое число: '))
    num2 = int(input('Введите еще одно целое число: '))

    print(f'Наибольший общий делитель этих двух чисел равен {gcd(num1, num2)}.')

def gcd(num1, num2):
    if num1 % num2 == 0: return num2
    else: return gcd(num1, num1 % num2)

if __name__ == '__main__': main()
