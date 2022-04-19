import cellphone

def cell_phone_test():
    phone = cellphone.CellPhone(input("Производитель: "), input("Номер модели:  "), float(input("Розничная цена: ")))
    print(f'Прозводитель: {phone.get_manufact()}')
    print(f'Номер модели: {phone.get_model()}')
    print(f'Розничная цена: {phone.get_retail_price():.2f}')

cell_phone_test()