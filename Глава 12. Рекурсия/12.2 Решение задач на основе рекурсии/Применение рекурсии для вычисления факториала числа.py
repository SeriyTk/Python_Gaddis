def main():
    number = int(input('Неотрицательное целое число: '))
    print(f'Факториал числа {number} равняется {factorial(number)}.')

def factorial(num):
    if num == 0: return 1
    else: return num * factorial(num - 1)
if __name__ == '__main__': main()