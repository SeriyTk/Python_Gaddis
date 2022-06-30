def main():
    total = 0
    sum_list = [float(input(f'Сумма за день №{day + 1}: ')) for day in range(7)]
    print(sum_list)
    for i in sum_list: total += i
    print(total)


main()
