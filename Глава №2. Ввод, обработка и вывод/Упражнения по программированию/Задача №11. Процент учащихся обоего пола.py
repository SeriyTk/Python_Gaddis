def Student_Percentage():
    mens = int(input('Количество мужщин: '))
    womens = int(input('Количество женщин: '))
    total = mens + womens
    print(f'''
Процент мужщин {mens / total:.0%}
процент женщин {womens / total:.0%}
''')


if __name__ == '__main__': Student_Percentage = Student_Percentage()
