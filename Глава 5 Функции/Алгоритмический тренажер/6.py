import random as r


def rand_num(start, end):
    return r.randint(start, end)


rand = rand_num(1, 100)
print(rand)
