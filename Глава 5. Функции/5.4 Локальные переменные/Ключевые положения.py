"""
Локальная переменная создается внутри функции. Инструкции, которые находятся за
пределами функции, к ней доступа не имеют. Разные функции могут иметь локальные
переменные с одинаковыми именами, потому что функции не видят локальные переменные друг друга.
"""
def main(): get_name(); print('Привет, ', name)

def get_name(): name = input('Введите свое имя: ')

main()