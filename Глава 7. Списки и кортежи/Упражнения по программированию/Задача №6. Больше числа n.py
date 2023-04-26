def main():
    list_num = [i for i in range(20)]
    number = int(input('Введите число: '))
    get_numbers(list_num, number)

def get_numbers(list, n):
    for num in list:
        if num > n: print(num)

if __name__ == '__main__': main()