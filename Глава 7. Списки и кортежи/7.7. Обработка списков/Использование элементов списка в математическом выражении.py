NUM_EMPLOYEES = 6
def main():
    hours = [i for i in range(NUM_EMPLOYEES)]
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(input(f'Bвeдитe число отработанных часов сотрудником №{index + 1}: '))
    print()
    pay_rate = float(input('Bвeдитe почасовую ставку оплаты: '))
    print()
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'Зapплaтa сотрудника {index + 1}: ${gross_pay :,.2f}')

if __name__ == '__main__': main()