import random as r
print(r.randint(1, 100))
print()
def random_numbers():
    print(f'Число равняется {r.randint(1, 10)}')
if __name__ == '__main__': random_numbers()
print()
def random_numbers2():
    for i in range(5): print(f'Число равняется {r.randint(1, 100)}')

if __name__ == '__main__': random_numbers2()