def Student_Percentage():
    mans = int(input('Количество учащихся мужского пола: '))
    femans = int(input('Количество учащихся женского пола: '))
    total_students = mans + femans
    print('Процент юношей', format(mans / total_students, '.0%'), 'процент девушек', format(femans / total_students, '.0%'))


Student_Percentage()
