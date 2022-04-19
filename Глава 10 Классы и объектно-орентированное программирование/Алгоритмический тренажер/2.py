class Book:
    def __init__(self, title, author, publisher):
        self.__book_title = title
        self.__author_name = author
        self.__publisher_name = publisher

    def set_book_title(self, title):
        self.__book_title = title
    def set_author_name(self, author):
        self.__author_name = author
    def set_publisher_name(self, publisher):
        self.__publisher_name = publisher

    def get_book_title(self):
        return self.__book_title
    def get_author_name(self):
        return self.__author_name
    def get_publisher_name(self):
        self.__publisher_name

        def __str__(self):
            return (f'''
    Заголовок книги: {self.__book_title}
    Имя автора: {self.__author_name}
    Имя издателя: {self.__publisher_name}
    ''')