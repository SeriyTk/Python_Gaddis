import random as rnd
def main():
    list_num = [rnd.randint(0, 9) for i in range(7)]
    for i in list_num: print(i)

if __name__ == '__main__': main()