import random as rm
def dice(start, end):
    answer = 'д'
    while answer:
        print(rm.randint(start, end))
        print(rm.randint(start, end))
        print('Хотите бросать еще?')
        print("Если - да, введите 'д', а иначе любое значение.")
        answer = input(': ')
        if answer !='д':
            print('Программа завершена.')
            break
            
dice(1,6)