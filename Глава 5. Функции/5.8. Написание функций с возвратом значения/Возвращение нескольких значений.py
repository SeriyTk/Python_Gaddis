'''return выражение1, выражение2, . . . '''
def get_name(): return input('Введите свое имя: '), input('Введите свою фамилию: ')
first_name, last_name = get_name()
if __name__ == '__main__': print(first_name, last_name)
