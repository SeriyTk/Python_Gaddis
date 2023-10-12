def test_score_average():
    test1 = float(input('Bвeдитe первую оценку: '))
    test2 = float(input('Bвeдитe вторую оценку: '))
    test3 = float(input('Bвeдитe третью оценку: '))
    average = (test1 + test2 + test3) / 3.0
    print('Средний балл составляет', average)


if __name__ == '__main__': test_score_average()
