'''
значение in список
'''
def main():
    prod_nums = ['V475', 'F987', ' Q143', 'R688']
    search = input('Номер изделия: ')
    if search in prod_nums: print(f'{search} найден.')
    else: print(f'{search} не найден.')

main()