list1 = [i for i in range(1, 5)]
list2 = list1
print(list1)
print(list2)
list1[0] = 45
print(list1)
print(list2)
print()
list1 = [i for i in range(1, 5)]
list2 = [] + list1
print(list2)
