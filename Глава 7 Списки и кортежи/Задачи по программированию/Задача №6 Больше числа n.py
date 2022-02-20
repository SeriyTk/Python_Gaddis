num_list = [1, 2, 3, 4, 5, 6, 7]


def More_than_n(par1, par2):
    for i in par1:
        if i > par2:
            print(i)
        else:
            continue


More_than_n(num_list, 2)
