PAY = 145000.00
INCREASE = 0.03
YEARS = 6
def Fee_increase():
    print('Год \tПлата')
    print('---------------')
    print(f'1 \t\t{PAY}')
    pay = PAY
    for year in range(2, YEARS + 1): pay += (PAY * INCREASE); print(f'{year} \t\t{pay:.2f}')


if __name__ == '__main__': Fee_increase = Fee_increase()
