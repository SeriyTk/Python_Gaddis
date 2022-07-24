import modules1 as m1


def main():
    numb = m1.get_audience_number()
    teach = m1.get_teacher()
    tm = m1.get_times()
    сourse_number = input("Введите номер курса: ")
    numb1 = numb.get(сourse_number, 'Такого курса нет.')
    teach1 = teach.get(сourse_number)
    tm1 = tm.get(сourse_number)
    print(f'''
    Курс номер {сourse_number}:
    аудитория: {numb1};
    преподаватель: {teach1};
    время: {tm1}.
    ''')


main()
