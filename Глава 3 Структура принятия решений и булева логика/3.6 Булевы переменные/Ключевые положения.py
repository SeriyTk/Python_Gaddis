# Булева, или логическая, переменная может ссылаться на одно из двух значений:
#  True (Истина) или False (Ложь). Булевы переменные обычно применяются в качестве флагов,
# которые указывают на наличие каких-то конкретных условий.
def sales_quota():
    sales = float(input('Сумма продаж:'))
    if sales >= 50000:
        sales_quota_met = True
    else:
        sales_quota_met = False


    if sales_quota_met:
        print('Вы выполнили план.')
    else:
        print('План не выполнен.')

sales_quota()