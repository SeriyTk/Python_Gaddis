def main():
    numbers = [i for i in range(2, 11, 2)]
    print(f'Сумма составляет {get_total(numbers)}')

def get_total(numbers):
    total = 0
    for num in numbers: total += num
    return total


main()
