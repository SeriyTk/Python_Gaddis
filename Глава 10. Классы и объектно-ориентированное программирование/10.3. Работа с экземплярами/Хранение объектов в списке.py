import cellphone_list as CP_L
def main():
    phones = make_list()
    display_list(phones)
def make_list():
    phone_list = []
    print('Введите данные о пяти телефонах.')
    for i in range(5):
        print(f'Телефон №{i + 1}: ')
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Розничная цена: '))
        print()
        phone = CP_L.CellPhone(man, mod, retail)
        phone_list.append(phone)
    return phone_list
def display_list(phone_list):
    for j in phone_list:
        print(j.get_manufact())
        print(j.get_model())
        print(j.get_retail_price())
        print()

if __name__ == '__main__': main()
