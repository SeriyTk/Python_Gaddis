def main():
    n = int(input('Число: '))
    for number in range(1, n): print(fun(number),end=' ')



def fun(n):
    if n == 1: return 1
    elif n != 1: fun(n-1); return n
if __name__ == '__main__': main()