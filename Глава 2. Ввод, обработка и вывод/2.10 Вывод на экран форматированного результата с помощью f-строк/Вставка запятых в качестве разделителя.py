number = 1234567890.12345
print(f'{number:,}')
print(f'{number:,.2f}')
print()
def dollar_display():
    monthly_pay = 5000.0
    annual_pay = monthly_pay * 12
    print(f'Baшa годовая зарплата составляет ${annual_pay:,.2f} ')

dollar_display()