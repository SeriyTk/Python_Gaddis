class Savings_Account:
    def __init__(self, account_num, int_rate, bal):
        self.__acc_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    def set_acc_num(self, account_num): self.__acc_num = account_num
    def set_int_rate(self, int_rate): self.__interest_rate = int_rate
    def set_bal(self, bal): self.__balance = bal

    def get_acc_num(self): return self.__acc_num
    def get_int_rate(self): return self.__interest_rate
    def get_bal(self): return self.__balance

    def __str__(self): return f'''
Вот введенные Вами данные:
-----------------------------------------------------------------------------
Номер счета: {self.get_acc_num()}
Процентная ставка: {self.get_int_rate()}
Остаток: {self.get_bal()}
'''

class CD(Savings_Account):
    def __init__(self, account_num, int_rate, bal, mat_date):
        Savings_Account.__init__(self, account_num, int_rate, bal)
        self.__maturity_date = mat_date

    def set_mat_date(self, mat_date): self.__maturityt_date = mat_date

    def get_mat_date(self): return self.__maturity_date

    def __str__(self): return f'''
Cчeт депозитного сертификата (CD):
-----------------------------------------------------------------------------
Номер счета: {self.get_acc_num()}
Процентная ставка: {self.get_int_rate()}
Остаток: {self.get_bal()}
Дата погашения: {self.get_mat_date()}
    '''