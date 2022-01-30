def feet_to_inches(feet):
    return feet * 12


feet = int(input('Количество футов: '))
print(f'Получается {feet_to_inches(feet)} дюйма.')
