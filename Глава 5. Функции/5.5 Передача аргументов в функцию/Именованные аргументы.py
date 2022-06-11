def main():
    show_interest(rate=0.01, periods=10, principal=10000.0)


def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f'Пpocтoй процентный доход составит$ {interest:.2f}')


main()
