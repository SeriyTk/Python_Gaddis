class Information:
    def __init__(self, name, adress, age, phone):
        self.name = name
        self.adress = adress
        self.age = age
        self.phone = phone

    def get_name(self):
        return self.name
    def get_adress(self):
        return self.adress
    def get_age(self):
        return self.age
    def get_phone(self):
        return self.phone

    def __str__(self):
        return (f'''
Имя: {self.name}
Адрес: {self.adress}
Возвраст: {self.age}
Телефон: {self.phone}
''')

def info():
    for i in range(3):
        print('Введите данные')
        name = input(f'Имя {i+1}: ')
        adress = input(f'Адрес {i+1}: ')
        age = input(f'Возвраст {i+1}: ')
        phone = input(f'Телефон {i+1}: ')
        info = Information(name, adress, age, phone)
        print(info)

info()