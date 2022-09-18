'''
Процедурное программирование представляет собой методику написания программного
обеспечения . Это практика программирования, в центре внимания которого находятся
процедуры или действия, происходящие в программе.
Основой объектно-ориентированного программирования служат объекты, которые создаются из абстрактных типов
данных, объединяющих данные и функции.
'''
class Purse:
   def __init__(self,valuta, name = ': '):
      if valuta not in ('USD', 'EUR'): raise ValueError
      self.__money = 0.00
      self.valuta = valuta
      self.name = name

   def up_balance(self, howmoney): self.__money += howmoney; return howmoney

   def down_balance(self,howmoney):
      if self.__money - howmoney < 0:print('Мало денег.'); raise ValueError('Мало денег.')
      else: self.__money -= howmoney
      return howmoney

   def info(self): return self.__money

   def __del__(self): print('Удаление')

x = Purse('USD')
y = Purse('USD','Вася')
y.up_balance(10)

x.money = -200
x.up_balance(y.down_balance(7))
print(x.info())
print(y.info())
