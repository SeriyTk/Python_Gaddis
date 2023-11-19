SAUSAGES_PER_PACK = 10
BUNS_PER_PACK = 8
def Sausage_calculator():

    # Запросите у пользователя количество участников и хот-догов на человека
    participants = int(input("Введите количество участников пикника: "))
    hot_dogs_per_person = int(input("Введите количество хот-догов на одного участника: "))

    # Рассчитайте общее количество хот-догов
    total_hot_dogs = participants * hot_dogs_per_person


    # Рассчитайте необходимое количество упаковок с сосисками и булочками
    sausage_packs_needed = (total_hot_dogs + SAUSAGES_PER_PACK - 1) // SAUSAGES_PER_PACK
    bun_packs_needed = (total_hot_dogs + BUNS_PER_PACK - 1) // BUNS_PER_PACK

    # Рассчитайте количество оставшихся сосисок и булочек
    remaining_sausages = sausage_packs_needed * SAUSAGES_PER_PACK - total_hot_dogs
    remaining_buns = bun_packs_needed * BUNS_PER_PACK - total_hot_dogs

    # Выведите результаты
    print(f'''
Минимально необходимое количество упаковок с сосисками: {sausage_packs_needed},
Минимально необходимое количество упаковок с булочками: {bun_packs_needed},
Количество оставшихся сосисок: {remaining_sausages},
Количество оставшихся булочек: {remaining_buns}.
''')

if __name__ == '__main__': Sausage_calculator = Sausage_calculator()
