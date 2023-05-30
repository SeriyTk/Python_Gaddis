class Employee:
    def __init__(self, name, id, dept, post):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__post = post

    def set_name(self, name): self.__name = name
    def set_id(self, id): self.__id = id
    def set_dept(self, dept): self.__dept = dept
    def set_post(self, post): self.__post = post

    def get_name(self): return self.__name
    def get_id(self): return self.__id
    def get_dept(self): return self.__dept
    def get_post(self): return self.__post

    def __str__(self): return f'''
Имя: {self.__name};
ИД: {self.__id};
Отдел: {self.__dept};
Должность: {self.__post}.
'''

