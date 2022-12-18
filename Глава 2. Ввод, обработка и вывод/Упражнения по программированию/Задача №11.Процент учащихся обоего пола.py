def Student_Percentage():
    men = int(input('Количество учащихся мужского пола: '))
    women = int(input('Количество учащихся женского пола: '))
    percentage_men = men / (men + women)
    percentage_women = women / (men + women)
    print(f'''
Процент юношей: {percentage_men:.0%}
Процент девушек: {percentage_women:.0%}
''')

Student_Percentage()