'''множество1.issubsеt(множество2)'''
set1 = set ([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1 >= set2)
print(set1 <= set2)
