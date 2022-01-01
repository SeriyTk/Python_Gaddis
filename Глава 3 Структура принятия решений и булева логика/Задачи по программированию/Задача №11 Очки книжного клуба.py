def Book_Club_Points():
    number_of_books = int(input('Количество купленных книг: '))
    if 2 <= number_of_books < 4:
        print(5)
    elif 4 <= number_of_books < 6:
        print(15)
    elif 6 <= number_of_books < 8:
        print(30)
    elif number_of_books >= 8:
        print(60)
    else:
        print(0)


Book_Club_Points()
