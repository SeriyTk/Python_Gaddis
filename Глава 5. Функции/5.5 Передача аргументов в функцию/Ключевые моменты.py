"""
Аргумент - это любая порция данных, которая передается в функцию, когда функция
вызывается.
 Параметр- это переменная, которая получает аргумент, переданный в функцию.
"""
def main(): value = 5; show_double(value)

def show_double(number): result = number * 2; print(result)

main()