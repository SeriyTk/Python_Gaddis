def main():
    my_sum = range_sum([i for i in range(1, 10)], 2, 5)

    print(f'Сумма значений с 2 по 5 позицию равняется {my_sum}')

def range_sum(num_list, start, end):
    if start > end: return 0
    else: return num_list[start] + range_sum(num_list, start + 1, end)

if __name__ == '__main__': main()