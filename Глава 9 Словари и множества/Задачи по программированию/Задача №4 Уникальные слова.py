def input_file():
    with open(r'G:\answers.txt') as in_file:
        print('Содержание файла.')
        unic = set()
        for i in in_file:
            print(i.rstrip())
            unic.add(i.rstrip())
        print()
        print("Уникальные элементы.")
        print(unic)



def Unique_words():
    input_file()


Unique_words()
