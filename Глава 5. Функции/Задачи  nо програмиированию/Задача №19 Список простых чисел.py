def main():
    for i in range(1, 101): is_prime(i)


def is_prime(number):
    x = number // 2
    while x > 1:
        if number % x == 0:
            print(f'{number} имеет делитель {x}'); break; x -= 1
        else:
            print(f'{number} является простым'); break

main()



