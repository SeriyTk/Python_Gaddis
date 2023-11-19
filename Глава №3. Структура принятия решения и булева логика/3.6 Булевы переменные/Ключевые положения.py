def main():
    hungry = True
    sleepy = False
    sales = float(input('Квота: '))
    if sales >= 50000.0: sales_quota_met = True
    else: sales_quota_met = False

    if sales_quota_met: print('Вы выполнили свою квоту продаж!')
    else: print('Вы не выполнили свою квоту продаж!')



if __name__ == '__main__': main()
