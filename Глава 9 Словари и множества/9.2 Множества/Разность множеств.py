# Разность множества1 и множества2- это все элементы множестваl, не входящие в множество2.
# В Python для получения разности двух множеств вызывается метод difference ().
# Вот общий формат вызова:
# множество1.diffеrеnсе(множество2)
set1 = set( [1, 2, 3, 4] )
set2 = set( [3, 4, 5, 6] )
set3 = set1.difference(set2)
print(set3)
# Для нахождения разности двух множеств можно также использовать оператор -. Вот общий
# формат выражения с использованием оператора - с двумя множествами:
# множество1 - множество2
set1 = set( [1, 2, 3, 4] )
set2 = set( [3, 4, 5, 6] )
set3 = set2 - set1
print(set3)