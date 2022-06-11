def main():
    ass_val = assessed_value(float(input("Фактическая стоимость: ")))
    print(f'Оценочная стоимость {ass_val}')
    print(f'Налог на имущество {property_tax(ass_val)}')



def assessed_value(par): return par * 0.6
def property_tax(par): return (par * 0.72) / 100

main()
