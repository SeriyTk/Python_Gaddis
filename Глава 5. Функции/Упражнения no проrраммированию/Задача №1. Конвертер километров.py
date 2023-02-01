MIL = 0.6214
def Kilometer_converter():
    kil = int(input('Введите километры: '))
    print(f'Километры:{kil} - мили:{kil * MIL: .2f}')

if __name__ == '__main__': Kilometer_converter()