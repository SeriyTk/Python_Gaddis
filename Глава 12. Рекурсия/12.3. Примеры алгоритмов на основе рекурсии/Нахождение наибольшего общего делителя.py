def main():
    num1 = int(input('Введите целое число: '))
    num2 = int(input('Введите еще одно целое число: '))
    print(f'Наибольший обший делитель этих двух чисел равен {gcd(num1, num2)}.')
def gcd(x, y):
    if x % y == 0: return y
    else: return gcd(x, x % y)
if __name__ == '__main__': main()
