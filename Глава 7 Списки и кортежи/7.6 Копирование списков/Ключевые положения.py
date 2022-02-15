# Для создания копии списка необходимо скопировать элементы списка.
# обе переменные listl и list2 будут ссылаться на один и тот же список в оперативной памяти.
list1  = [1, 2, 3, 4]
print(list1)
list2 = list1
print(list2)
# обе переменные list1 и list2 будут ссылаться на два отдельных, но идентичных списка.
list2 = []
for item in list1:
    list2.append(item)
# или
ist2 = [] + list1
print(list2)