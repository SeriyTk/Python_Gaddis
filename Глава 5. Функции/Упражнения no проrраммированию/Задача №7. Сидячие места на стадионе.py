A = 20
B = 15
C = 10
def Seat_place():
    total_sum = 0
    total_A = 0
    total_B = 0
    total_C = 0
    while True:
        klass = input('Билеты какого класса (A, B, C): ')
        if klass == '': break
        elif klass != "A" and klass != "B" and klass != "C": print('Неверный класс.')
        else:
            if klass == 'A':
                tickets_A = int(input('Количество билетов А: '))
                total_A = tickets_A
                total_sum += A * tickets_A
            elif klass == 'B':
                tickets_B = int(input('Количество билетов B: '))
                total_B = tickets_B
                total_sum += B * tickets_B
            elif klass == 'C':
                tickets_C = int(input('Количество билетов C: '))
                total_C = tickets_C
                total_sum += C * tickets_C

    print(f'''
Было продано билетов класса А: {total_A};
было продано билетов класса B: {total_B};
было продано билетов класса C: {total_C};
сумма дохода, полученного от продажи билетов {total_sum}           
''')

if __name__ == '__main__': Seat_place()