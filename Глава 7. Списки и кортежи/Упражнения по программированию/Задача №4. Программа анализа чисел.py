NUM = 5
def main():
    list_num = [int(input('Введите число: ')) for num in range(NUM) ]
    sum_num = get_sum_num(list_num)
    average = get_average(list_num, sum_num)
    print(f'''
Наименьшее число: {min(list_num)}
наибольшее число: {max(list_num)}
сумма чисел: {sum_num}
среднее арифметическое: {average}
''')

def get_sum_num(list):
    total = 0
    for i in list: total += i
    return total
def get_average(list, sum): return sum / len(list)

if __name__ == '__main__': main()