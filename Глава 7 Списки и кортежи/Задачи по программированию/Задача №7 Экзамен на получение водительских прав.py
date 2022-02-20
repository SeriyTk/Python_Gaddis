def write_subjects_answers():
    with open(r'G:\answers.txt', 'w') as f_answ:
        for i in range(20):
            print(input(f'Ответ на вопрос №{i + 1}: '), file=f_answ)

    print('Все ответы записаны в файл.')

def list_subjects_answers():
    list_answer = []
    with open(r'G:\answers.txt') as f_answ:
        line = f_answ.readline()
        while line != '':
            list_answer.append(line.rstrip())
            line = f_answ.readline()
    return list_answer




def Examination_on_obtaining_a_driver_license(par):
    right_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    r_answers = 0
    w_answers = 0
    l_w_answers = []
    for i in range(len(par)):
        if par[i] == right_answers[i]:
            r_answers += 1
        else:
            w_answers += 1
            l_w_answers.append(i +1)
    if 15 <= r_answers <= 20:
        print('Экзамен сдан.')
    else:
        print("Экзамен не сдан.")

    print(f'''
Количество правильных ответов {r_answers};
количество не правильных ответов {w_answers};
номера вопросов, ответы на которые были не правильные {l_w_answers}.
''')

        
        
Examination_on_obtaining_a_driver_license(list_subjects_answers())
