def show_sum(num1, num2):
    print(num1 + num2)


def string_args():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    reverse_name(first_name, last_name)


def reverse_name(first_name, last_name):
    print(last_name, first_name)


string_args()
