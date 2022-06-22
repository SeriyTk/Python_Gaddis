def main():
    total = 0
    for i in open(input("Имя файла: ")):
        total += 1
        if total <= 5: print(i, end='')



main()
