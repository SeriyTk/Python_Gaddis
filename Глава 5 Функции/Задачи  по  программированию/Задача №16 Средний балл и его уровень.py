def Average_score_and_its_level():
    grades = 0
    total = 0
    for i in range(5):
        grade = int(input(f'Введите оценку №{i + 1}: '))
        print(determine_grade(grade))
        grades += grade
        total += 1
    print(f'Средний бал {calc_average(grades, total)}.')


def calc_average(grades, total):
    return grades / total

def determine_grade(grade):
    if grade >= 90:
        return 'A'
    elif 80 <= grade < 90:
        return 'B'
    elif 70 <= grade < 80:
        return 'C'
    elif 60 <= grade < 70:
        return 'D'
    else:
        return 'E'


Average_score_and_its_level()
