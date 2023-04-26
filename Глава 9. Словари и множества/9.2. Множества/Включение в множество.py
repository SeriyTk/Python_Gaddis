set1 = set ([1, 2 , 3, 4, 5 ])
set2 = {item for item in set1}
print(set2)
set3 = {item ** 2  for item in set1}
print(set3)
set3 = {item ** 2  for item in set1 if item < 10}
print(set3)