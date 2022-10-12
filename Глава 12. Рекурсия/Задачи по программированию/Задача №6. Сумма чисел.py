def main():
    print(sum_numbers(int(input('Введите число: '))))


def sum_numbers(n):
    if n == 1: return 1
    return n + sum_numbers(n - 1)

if __name__ == '__main__': main()