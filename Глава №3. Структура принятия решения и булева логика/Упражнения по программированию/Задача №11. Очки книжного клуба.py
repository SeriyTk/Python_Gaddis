def Book_Club_Points():
    number_books = int(input('Количество книг: '))
    if number_books <= 1: print('0 очков.')
    elif number_books == 2 or number_books == 3: print('5 очков.')
    elif number_books == 4 or number_books == 5: print('15 очков.')
    elif number_books == 6 or number_books == 7: print('30 очков.')
    else: print('60 очков.')


if __name__ == '__main__': Book_Club_Points = Book_Club_Points()
