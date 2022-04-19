from modules import Retailltem

def  retailltem():
    for i in range(1,4):
        product = Retailltem(input('Описание: '), input("Количество: "), input("Цена: "))
        print(f'Товар №{i} {product}')

retailltem()


