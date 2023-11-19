HIGH_SCORE = 95
def test_average():
    test1 = int(input('Введите оценку №1: '))
    test2 = int(input('Введите оценку №2: '))
    test3 = int(input('Введите оценку №3: '))
    average = (test1 + test2 + test3) / 3

    print(f'Средний бал {average:.1f}')

    if average >= HIGH_SCORE: print('Поздравляем! Отличный средний балл!')

if __name__ == '__main__': test_average = test_average()
