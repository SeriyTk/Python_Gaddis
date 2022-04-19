import cellphone

def cell_phone_list():
    # Получить список объектов CellPhone.
    phones_list = cellphone.make_list()
    # Показать данные в списке.
    print('Boт введенные Вами данные: ')
    cellphone.display_list(phones_list)

cell_phone_list()
