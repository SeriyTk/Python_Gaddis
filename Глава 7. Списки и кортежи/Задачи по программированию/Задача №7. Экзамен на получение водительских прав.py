import exams

def main():
    exams.answer_options()
    '''
    exams.writer_list(exams.answers_on_questions())
    '''
    list_answers = exams.read_file('answers')
    print(list_answers)

main()
