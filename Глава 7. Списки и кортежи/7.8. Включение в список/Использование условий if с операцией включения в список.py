list1= [1, 12, 2, 20, 3, 15, 4]
list2 = []
for n in list1:
    if n <10: list2.append(n)
print(list2)
print()
list2 = [item for item in list1 if item < 10]
print(list2)
print()
last_names = ['Джекеон', 'Смит', 'Хильдебрандт', 'Джонс']
short_names = [name for name in last_names if len(name) < 6]
print(short_names)