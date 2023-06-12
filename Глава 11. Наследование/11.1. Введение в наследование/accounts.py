class SavingsAccount:
    def __init__(self, acc_num, int_rate, bal):
        self.__acc_num = acc_num
        self.__int_rate = int_rate
        self.__bal = bal

    def set_acc_num(self, acc_num): self.__acc_num = acc_num
    def set_int_rate(self, int_rate):self.__int_rate = int_rate
    def set_bal(self, bal): self.__bal = bal

    def get_acc_num(self): return self.__acc_num
    def get_int_rate(self): return self.__int_rate
    def get_bal(self): return self.__bal

    def __str__(self): return f'''
Вот введенные Вами данные:

Сберегательный счет
---------------------------
Hoмep счета: {self.__acc_num}
Процентная ставка: {self.__int_rate}
Ocтaтoк: {self.__bal:,.2f}
'''

class CD(SavingsAccount):
    def __init__(self, acc_num, int_rate, bal, mat_date):
        SavingsAccount.__init__(self, acc_num, int_rate, bal)
        self.__mat_date = mat_date
    def set_mat_date(self, mat_date): self.__mat_date = mat_date

    def get_mat_date(self): return self.__mat_date

    def __str__(self): return f'''
Дaтa по гашения: {self.__mat_date}
'''

