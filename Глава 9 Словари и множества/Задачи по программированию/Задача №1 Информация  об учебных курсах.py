def dct_key_audience(list_key, list_num_audience):
    key_audience  = {}
    for i in range(len(list_key)):
        key_audience[list_key[i]] = list_num_audience[i]
    return key_audience

def dct_key_teachers(list_key, list_teachers):
    key_teachers = {}
    for i in range(len(list_key)):
        key_teachers[list_key[i]] = list_teachers[i]
    return key_teachers

def dct_key_times(list_key, list_times):
    key_times = {}
    for i in range(len(list_key)):
        key_times[list_key[i]] = list_times[i]
    return key_times

def Information_about_training_courses():
    list_key = ['CS101','CS102','CS103','CS104','CS105']
    list_num_audience = [3004, 4501, 6755, 1244, 1411]
    list_teachers = ['Хайнс', 'Альварадо', 'Рич', 'Берк', 'Ли']
    list_times = ['8:00', '9:00', '10:00', '11:00', '13:00']
    audience = dct_key_audience(list_key, list_num_audience)
    teachers = dct_key_teachers(list_key, list_teachers)
    times = dct_key_times(list_key, list_times)
    course_number = input('Введите номер курса: ')
    if course_number in list_key:
        print(f'Курс №{course_number},  аудитория №{audience[course_number]}, преподаватель: {teachers[course_number]}, начало занятий {times[course_number]}.')
    else:
        print('Такого нет.')

Information_about_training_courses()