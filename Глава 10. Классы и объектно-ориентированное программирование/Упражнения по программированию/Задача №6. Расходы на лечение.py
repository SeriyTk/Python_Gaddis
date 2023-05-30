import treatment as tr
def main():
    init = input('Фамилия, имя, отчество: ')
    adres = input('Aдрес, город, область и почтовый индекс: ')
    phone = input('Телефонный номер: ')
    last_phone = input('Имя и телефон контактного лица для экстренной связи: ')
    patient = tr.Patient(init, adres, phone, last_phone)
    proc_list = []
    for i in range(int(input('Количество процедур: '))):
        title = input('Название процедуры: ')
        date = input('Дата: ')
        name = input('Врач: ')
        price = float(input('Стоимость: '))
        procedure = tr.Procedure(title, date, name, price)
        proc_list.append(procedure)
    print()
    print('Данные пациента')
    print("---------------------------------------")
    print(patient)
    print('Процедуры.')
    print('-----------------------------------------------')
    n = 1
    for j in proc_list: print(f'Процедура №{n}{j}'); n += 1


if __name__ == '__main__': main()
