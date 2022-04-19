import pickle, cellphone


def pickle_cellphone(par):
    with open(par, 'wb') as outfile:
        while True:
            # Получить данные о сотовом телефоне и создать объект CellPhone.
            phone = cellphone.CellPhone(input("Производитель: "),
                                        input("Модель: "), float(input("Розничная цена: ")))

            # Законсервировать объект и записать его в файл.
            pickle.dump(phone, outfile)

            # Получить еще один элемент данных?
            if input('Ещё один элемент данных? (д/н): ').lower() != 'д':
                print('Данные записаны')
                break


def unplckle_cellphone(par):
    with open(par, 'rb') as inpfile:
        end_file = False  # Флаг конца файла

        # Читаем до конца файла
        while not end_file:
            try:
                # Расконсервируем объект
                phone = pickle.load(inpfile)

                # Показать данные о телефоне
                cellphone.display_data(phone)
            except EOFError:
                end_file = True
