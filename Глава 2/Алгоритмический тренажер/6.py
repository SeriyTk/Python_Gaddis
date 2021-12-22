down_payment = float(input('Введите предоплату: '))
total = float(input('Введите итоговую сумму: '))
due = total - down_payment
print(f'К оплате {due:.2f}.')