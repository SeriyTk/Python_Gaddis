DAYS = 7
def main():
    list_sale = get_list_sale()
    total = get_total(list_sale)
    print(total)


def get_list_sale():
    list_sale = []
    for day in range(DAYS):
        sale = float(input(f'Сумма продаж за день №{day + 1}: '))
        list_sale.append(sale)
    return list_sale

def get_total(value_list):
    total = 0
    for num in value_list: total += num
    return total

if __name__ == '__main__': main()