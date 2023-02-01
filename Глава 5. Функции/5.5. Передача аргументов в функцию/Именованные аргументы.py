def keyword_args():
    show_interest(rate=0.01, periods=10, principal=10000.0)

def show_interest(rate, periods, principal):
    interest = principal * rate * periods
    print(f'Пpocтoй процентный доход составит ${interest:,.2f}')

if __name__ == '__main__': keyword_args()
print()
def keyword_string_args():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Baшe имя в обратном порядке')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last): print(last, first)

if __name__ == '__main__': keyword_string_args()