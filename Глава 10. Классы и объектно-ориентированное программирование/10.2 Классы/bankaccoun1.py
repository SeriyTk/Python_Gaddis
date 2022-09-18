class BankAccount:
    def __init__(self, bal): self.__balance = bal

    def deposit(self, amount): self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount: self.__balance -= amount
        else: print('Ошибка: недостаточно средств')

    def get_balance(self): return self.__balance

    # Метод __str__ возвращает строковое значение, сообщающее о состоянии объекта.
    def __str__(self): return f'Остаток составляет ${self.__balance:,.2f}'
