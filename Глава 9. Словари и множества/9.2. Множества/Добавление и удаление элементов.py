myset = set ()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
print()
myset = set([1, 2, 3])
myset.update([4, 5, 6])
print(myset)
print()
set1 = set([1, 2, 3])
set2 = set([8, 9, 10])
set1.update(set2)
print(set1)
print(set2)
print()
myset.remove(1)
print(myset)
print()
myset.clear()
print(myset)

