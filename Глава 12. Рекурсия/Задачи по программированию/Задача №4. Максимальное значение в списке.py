def main():
    print(GetMaxList([i for i in range(1, 21)]))

def GetMaxList(L):
    if L == []: return
    else:
        if len(L) > 1:
            # Получить максимум из следующих рекурсивных вызовов
            Max = GetMaxList(L[1:])

            # Сравнить максимум с первым элементом списка
            if L[0] < Max: return Max
            else: return L[0]

        if len(L) == 1: return L[0] # последний элемент в списке вернуть этот элемент

if __name__ == '__main__': main()