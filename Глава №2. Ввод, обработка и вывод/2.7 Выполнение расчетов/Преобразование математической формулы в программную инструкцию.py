
def future_value():
    future_value = float(input('Bвeдитe требуемое будущее значение: '))
    rate = float(input('Bвeдитe годовую процентную ставку: '))
    years = int(input('Bвeдитe количество лет хранения денег на счете: '))
    present_value = future_value / (1.0 + rate) ** years
    print('Baм потребуется внести сумму:', present_value)

if __name__ == '__main__': future_value()