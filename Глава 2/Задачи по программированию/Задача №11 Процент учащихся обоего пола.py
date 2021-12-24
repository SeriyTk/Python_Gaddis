def Percentage_students():
    men = int(input('Количество мужчин: '))
    women = int(input('Количество женщин: '))
    total_students = men + women
    print(f'''
    Процент учащихся мужского пола составляет {(men / total_students) * 100},
    процент учащихся женского пола составляет {(women / total_students) * 100}.
''')


Percentage_students()
