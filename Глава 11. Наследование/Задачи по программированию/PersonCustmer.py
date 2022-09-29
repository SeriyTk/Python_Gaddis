class Person:
    def __init__(self, name, adress, phone):
        self.__name = name
        self.__adress = adress
        self.__phone = phone

    def set_name(self, name): self.__name = name
    def set_adress(self, adress): self.__adress = adress
    def set_phone(self, phone): self.__phone = phone

    def get_name(self): return self.__name
    def get_adress(self): return self.__adress
    def get_phone(self): return self.__phone

class Custmer(Person):
    def __init__(self, name, adress, phone, num, answer):
        Person.__init__(self, name, adress, phone)
        self.__num = num
        self.__answer = answer

    def set_num(self, num): self.__num = num
    def set_answer(self, answer): self.__answer = answer

    def get_num(self): return self.__num
    def get_answer(self): return self.__answer

    def __str__(self): return f'''
  {self.get_name()} 
  {self.get_adress()}
  {self.get_phone()}
  {self.get_num()}
'''

