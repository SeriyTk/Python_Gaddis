def f_string_no_formatting():
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print(f'Ежемесячный платеж составляет {monthly_payment}. ')
if __name__ == '__main__': f_string_no_formatting()
def f_string_formatting():
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print(f'Ежемесячный платеж составляет {monthly_payment:.2f}. ')


if __name__ == '__main__': f_string_formatting()
