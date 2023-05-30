class BankAccount:
    def __init__(self, bal): self.__balavce = bal
    def deposit(self, amount): self.__balavce += amount
    def withdraw(self, amount):
        if self.__balavce >= amount: self.__balavce -= amount
        else: print('Ошибка: недостаточно средств')
    def get_balance(self): return self.__balavce
