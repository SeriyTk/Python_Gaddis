def answer_options():
    print('''
Варианты ответов:
A, B, C, D
    ''')

def answers_on_questions():
    list_answers =[input(f'Ответ на вопрос №{i + 1}: ') for i in range(20)]
    return list_answers

def writer_list(list):
    with open('answers', 'w') as outfile:
        for i in list: print(i, file=outfile)

def read_file(par):
    list_answers = [i.rstrip() for i in open(par)]
    return list_answers
