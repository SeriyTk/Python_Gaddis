class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def set_name(self,name): self.__name = name
    def set_id(self, id): self.__id = id

    def get_name(self): return self.__name
    def get_id(self): return self.__id

class ProductionWorke(Employee):
    def __init__(self, name, id, shift_num, rate):
        Employee.__init__(self, name, id)
        self.__shift_num = shift_num
        self.__rate = rate
    def set_shift_num(self, shift_num): self.__shift_num = shift_num
    def set_rate(self, rate): self.__rate = rate

    def get_shift_num(self): return self.__shift_num
    def get_rate(self): return self.__rate

class ShiftSupervisor(Employee):
    def __init__(self, name, id, shift_num, rate, annual_salary, annual_bonus):
        Employee.__init__(self, name, id)
        self.__shift_num = shift_num
        self.__rate = rate
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus
    def set_shift_num(self, shift_num): self.__shift_num = shift_num
    def set_rate(self, rate): self.__rate = rate
    def set_annual_salary(self, annual_salary): self.__annual_salary = annual_salary
    def set_annual_bonus(self, annual_bonus): self.__annual_bonus = annual_bonus

    def get_shift_num(self): return self.__shift_num
    def get_rate(self): return self.__rate
    def get_annual_salary(self): return self.__annual_salary
    def get_annual_bonus(self): return self.__annual_bonus