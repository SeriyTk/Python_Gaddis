import math as m
def square_root():
    number = float(input('Bвeдитe число: '))
    print(f'Квадратный корень из {number} составляет {m.sqrt(number)}.')

if __name__ == '__main__': square_root()
print()
def hypotenuse():
    с = m.hypot(float ( input ('Введите длину стороны А: ') ), float ( input ('Введите длину стороны B: ') ))
    print(f'Длинa гипотенузы составляет {с}.')

if __name__ == '__main__': hypotenuse()