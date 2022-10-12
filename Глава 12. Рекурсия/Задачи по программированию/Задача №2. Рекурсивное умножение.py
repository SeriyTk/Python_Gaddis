def main():
    print(mul(int(input('Введите число №1: ')), int(input('Введите число №2: '))))
def mul(x, y):
        if x == 1: return y
        return y + mul(x - 1, y)
if __name__ == '__main__': main()