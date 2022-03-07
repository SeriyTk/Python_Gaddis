# копируемое_строковое_значение * п
my_string = 'w' * 5
print(my_string)
print('Привет' * 5)


def repetition_operator():
    for count in range(1, 10):
        print('Z' * count)
    for count in range(8, 0, -1):
        print('Z' * count)


repetition_operator()
