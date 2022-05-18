def Personal_Information():
    reply = '''
    Меня зовут %(name)s;
    мой адрес %(adres)s;
    номер телефона %(phone)s;
    моя специализация %(specialization)s
    '''
    values = {'name': input('Введите имя: '),
              'adres': input('Введите адрес: '),
              'phone': input('Введите номер телефона: '),
              'specialization': input('Введите специализацию: ')
              }
    print(reply % values)


Personal_Information()
