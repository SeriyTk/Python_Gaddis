def Body_mass_index():
    body_mass = float(input('Ввести массу тела в кг.: '))
    body_height = float(input('Рост тела в метрах: '))
    body_mass_index = get_body_mass_index(body_mass, body_height)
    print(f'Индекс массы тела равен {body_mass_index:.2f}.')
    if body_mass_index < 18.5:
        print('Индекс массы тела ниже нормы.')
    elif 18.5 <= body_mass_index <= 25:
        print('Индекс массы тела оптимальный.')
    elif body_mass_index > 25:
        print('Индекс массы тела больше нормы.')


def get_body_mass_index(body_mass, body_height):
    body_mass_index = body_mass / body_height
    return body_mass_index

Body_mass_index()
