import random as rd

MIN= 1
MAX = 6

def main():
    while True:
        if input('Бросить кубики?(д =да): ') !='д': break
        else:
            print('Бросаем кубики ... ')
            print(rd.randint(MIN,MAX))
            print(rd.randint(MIN, MAX))

main()