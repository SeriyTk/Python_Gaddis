def get_sales_week(par):
    sales_list = []
    for day in range(par):
        sales_list.append(float(input(f'Введите сумму продаж за день недели №{day + 1}: ')))
    return sales_list

def get_total_sales(par):
    total = 0
    for sale in par:
        total += sale
    return total


def Total_Sales():
    WEEK = 7
    return get_total_sales(get_sales_week(WEEK))


print(f'Общая сумма продаж за неделю составляет {Total_Sales()}.')
