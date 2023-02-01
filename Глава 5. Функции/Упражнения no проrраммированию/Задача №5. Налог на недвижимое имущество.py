TAX = 0.60
PROPERTY_TAX = 0.72

def tax():
    actual_cost = float(input('Фактическая стоимость: '))
    estimated_cost = actual_cost * TAX
    property_tax = estimated_cost / 100 * PROPERTY_TAX
    print(f'Оценочная стоимость: {estimated_cost:,.2f}')
    print(f'Налог на имущество: {property_tax:.2f}')

if __name__ == '__main__': tax()