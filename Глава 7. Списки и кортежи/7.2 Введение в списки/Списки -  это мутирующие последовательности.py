NUM_DAYS = 5


def main():
    sales = [float(input(f'День №{day + 1}: ')) for day in range(NUM_DAYS)]

    for value in sales: print(value)


main()
