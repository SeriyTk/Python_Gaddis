START = 2
INCREASE = 0.3
DAYS = 10
def Population():
   increase = START
   print('День \tПопуляция')
   print(f'{1}      \t{START}')
   for day in range(2, DAYS + 1): increase += (increase * INCREASE);print(f'{day}      \t{increase}')



if __name__ == '__main__': Population = Population()
