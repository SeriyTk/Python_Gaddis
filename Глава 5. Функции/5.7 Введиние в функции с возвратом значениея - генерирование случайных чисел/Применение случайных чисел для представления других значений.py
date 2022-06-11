import random as rd

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if rd.randint(HEADS, TAILS) == HEADS: print ('Орел')
        else: print ('Решка')

main()
print()
print(rd.randrange(10,20, 5))