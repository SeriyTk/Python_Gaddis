def book_club_glasses():
    number_of_books = int(input('Количество приобретенных книг: '))
    if 2 <= number_of_books < 4: print('5 очков')
    elif 4 <= number_of_books < 6: print('15 очков')
    elif 6 <= number_of_books < 8: print('30 очков')
    elif 8 <= number_of_books: print('60 очков')
    else: print('0 очков')


book_club_glasses()
