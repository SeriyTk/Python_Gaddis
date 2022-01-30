INSURANCE = 0.8


def insurance_cost(cost):
    return cost * INSURANCE

print(insurance_cost(float(input('Стоимость строения: '))))
