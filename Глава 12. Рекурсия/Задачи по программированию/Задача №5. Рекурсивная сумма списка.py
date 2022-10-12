def main():
    print(CalcSumNumbers([i for i in range(1, 11)]))

def CalcSumNumbers(A):
    if A == []: return 0
    else:
        summ = CalcSumNumbers(A[1:])

        summ = summ + A[0]

        return summ

if __name__ == '__main__': main()