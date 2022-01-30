def Real_estate_tax(price):
    value_property = appraised_value_property(price)
    tax = property_tax(value_property)
    print(f'Оценочная стоимость {value_property:.2f}.')
    print(f'Налог на имущество {tax:.2f}.')


def appraised_value_property(price):
    return price * 0.6


def property_tax(value_property):
    return (value_property * 0.72) / 100


Real_estate_tax(10000)
