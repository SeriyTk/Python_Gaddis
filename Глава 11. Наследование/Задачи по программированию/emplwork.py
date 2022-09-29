class Employee:
    def __init__(self, name, num):
        self.__name = name
        self.__num_empl = num

    def set_name(self, name): self.__name = name
    def set_num_empl(self, num): self.__num_empl = num

    def get_name(self): return self.__name
    def get_num_empl(self): return self.__num_empl

    def __str__(self): return f'''
Данные сотрудника
Имя сотрудника: {self.get_name()}
Номер сотрудника: {self.get_num_empl()}
'''

class  ProductionWorker(Employee):
    def __init__(self, name, num_empl, number, rate):
        Employee.__init__(self, name, num_empl)
        self.__shift_number = number
        self.__wage_rate = rate

    def set_number(self, number): self.__shift_number = number
    def set_rate(self, rate): self.__wage_rate = rate

    def get_number(self): return self.__shift_number
    def get_rate(self): return self.__wage_rate

    def __str__(self): return f'''
Данные сотрудника
--------------------------------------------------------------------------------
Имя сотрудника: {self.get_name()}
Номер сотрудника: {self.get_num_empl()}
Номер смены: {self.get_number()}
Ставка почасовой оплаты труда: {self.get_rate()}
'''

class ShiftSupervisor(Employee):
    def __init__(self, name, num_empl, number, salary, bonus):
        Employee.__init__(self, name, num_empl)
        self.__shift_number = number
        self.__salary = salary
        self.__annual_bonus = bonus

    def set_number(self, number): self.__shift_number = number
    def set_salary(self, salary): self.__salary = salary
    def set_bonus(self, bonus): self.__annual_bonus = bonus

    def get_number(self): return self.__shift_number
    def get_salary(self): return self.__salary
    def get_bonus(self): return self.__annual_bonus

    def __str__(self): return f'''
Данные начальника смены
--------------------------------------------------------------------------------
Имя начальника смены: {self.get_name()}
Номер начальника смены: {self.get_num_empl()}
Номер смены: {self.get_number()}
Фиксированный оклад: {self.get_salary()}
Годовая премия: {self.get_bonus()}
'''