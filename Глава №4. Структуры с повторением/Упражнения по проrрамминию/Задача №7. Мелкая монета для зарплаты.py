def Small_coin():
    total = 0
    sum = 2
    days = int(input('Кол-во дней: '))
    print('Дни \t Монеты')
    for day in range(days):
        if (day + 1) == 1: print(f'{day + 1} \t \t 1 коп.')
        if (day + 1) == 2: print(f'{day + 1} \t \t {sum} коп.')
        if (day + 1) > 2: sum *= 2; total += sum; print(f'{day + 1} \t \t {sum} коп.')

    print(f'{(total + 3) / 100:,.2f}')



if __name__ == '__main__': Small_coin = Small_coin()
