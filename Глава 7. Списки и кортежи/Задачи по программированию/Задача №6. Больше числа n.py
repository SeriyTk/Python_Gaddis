def main():
    num_list = [i for i in range(1, 11)]
    print(num_list)
    n(num_list, int(input('Введите число: ')))

def n(par1, par2):
    for i in par1:
        if int(i) > par2: print(i, end=' ')


main()
