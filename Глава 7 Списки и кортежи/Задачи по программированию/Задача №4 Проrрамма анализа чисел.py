def list_number():
    num_list = []
    for n in range(20):
        num_list.append(int(input(f'Введите число №{n + 1}: ')))
    return num_list


def analysis_number(par):
    print(f'''
Наименьшее число в списке {min(par)};
наибольшее число в списке {max(par)};
сумма чисел в списке {sum(par)};
среднее арифметическое значение чисел в списке {sum(par) / len(par)}.
''')
    
    
analysis_number(list_number())
