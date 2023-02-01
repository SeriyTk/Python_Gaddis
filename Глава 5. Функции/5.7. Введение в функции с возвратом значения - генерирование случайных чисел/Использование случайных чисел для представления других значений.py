import random as r
HEADS = 1
TAILS = 2
TOSSES = 10
def coin_tos():
    for toss in range(TOSSES):
        if r.randint(HEADS, TAILS) == HEADS: print ( 'Орел' )
        else: print ('Решка' )

if __name__ == '__main__': coin_tos()