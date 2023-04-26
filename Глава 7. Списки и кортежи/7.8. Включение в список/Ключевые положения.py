list1 = [i for i in range(1, 5)]
list2 = []
for item in list1: list2.append(item)
print(list2)
list2 = [item for item in list1]
print(list2)
print()
list2 = [item ** 2 for item in list1]
print(list2)
print()
str_list = ['Мигнуть', 'Моргнуть', 'Кивнуть']
len_list = [len(s) for s in str_list]
print(len_list)