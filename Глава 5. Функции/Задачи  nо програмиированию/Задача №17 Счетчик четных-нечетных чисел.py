import random

ran_list = [random.randint(1, 100) for i in range(100)]
even = 0
odd = 0

for i in ran_list:
    if i % 2 == 0: even += 1
    else: odd +=1
print(ran_list)
print(f'Четных чисел {even}')
print(f'Нечетных чисел {odd}')

